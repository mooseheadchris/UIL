/**
 * Flashcard study + simplified SM-2 spaced repetition.
 *
 * Per (user, card) state:
 *   ef       — ease factor (default 2.5, floor 1.3)
 *   interval — days until nextDue
 *   reps     — consecutive successful reps since last lapse
 *   nextDue  — ISO date
 */

function todayStartIso_() {
  const d = new Date();
  d.setHours(0, 0, 0, 0);
  return d.toISOString();
}

function addDaysIso_(days) {
  const d = new Date();
  d.setHours(0, 0, 0, 0);
  d.setDate(d.getDate() + days);
  return d.toISOString();
}

/**
 * Given the current SRS state and a rating, return the new state.
 * Ratings must be SRS.RATING values (2/3/5).
 */
function srsUpdate_(state, rating) {
  let ef = state.ef || SRS.DEFAULT_EF;
  let interval = state.interval || 0;
  let reps = state.reps || 0;

  if (rating === SRS.RATING.HARD) {
    ef = Math.max(SRS.MIN_EF, ef - 0.15);
    interval = 1;
    reps = 0;
  } else if (rating === SRS.RATING.MEDIUM) {
    if (reps === 0) interval = 1;
    else if (reps === 1) interval = 6;
    else interval = Math.round(interval * ef);
    reps += 1;
  } else if (rating === SRS.RATING.EASY) {
    ef = ef + 0.1;
    if (reps === 0) interval = 4;
    else interval = Math.max(1, Math.round(interval * ef * 1.3));
    reps += 1;
  } else {
    throw new Error('Invalid rating: ' + rating);
  }
  return {
    ef: Math.round(ef * 100) / 100,
    interval: interval,
    reps: reps,
    nextDue: addDaysIso_(interval),
    lastReviewed: new Date().toISOString()
  };
}

/**
 * Return up to `limit` cards for the user in `subject` / `section`.
 * Due cards first, then new cards (capped by DAILY_NEW_CARD_CAP across
 * all subjects).
 *
 * Section filter rules:
 *   - falsy section → "All sections": include every matching-subject
 *     card, blank section included.
 *   - specific section → exact match only; cards with blank section are
 *     excluded.
 *
 * Response shape:
 *   { cards: [{cardId, subject, section, front, back}], dueCount, newAvailable }
 * (front/back are included — flashcard backs are not secret.)
 */
function getNextCards(token, subject, section, limit) {
  const claims = requireAuth(token);
  const subjectSel = subject || null;
  const sectionSel = section ? String(section).trim() : null;
  const cap = Math.min(Math.max(limit || SRS.DEFAULT_SESSION_SIZE, 1), 100);

  const progressRows = findWhere(SHEETS.STUDY_PROGRESS, function (r) {
    return r.userEmail === claims.email;
  });
  const progressByCard = {};
  progressRows.forEach(function (r) { progressByCard[r.cardId] = r; });

  const allCards = readAll(SHEETS.FLASHCARDS).filter(function (c) {
    if (subjectSel && c.subject !== subjectSel) return false;
    if (sectionSel && String(c.section || '').trim() !== sectionSel) return false;
    return true;
  });

  const today = todayStartIso_();
  const due = [];
  const fresh = [];
  allCards.forEach(function (c) {
    const p = progressByCard[c.cardId];
    if (!p) { fresh.push(c); return; }
    if (p.nextDue && String(p.nextDue) <= today) due.push({ card: c, due: p.nextDue });
  });

  due.sort(function (a, b) { return String(a.due) < String(b.due) ? -1 : 1; });

  const newReviewedToday = progressRows.filter(function (r) {
    return r.reps === 1 && r.lastReviewed && String(r.lastReviewed).slice(0, 10) === today.slice(0, 10);
  }).length;
  const newBudget = Math.max(0, SRS.DAILY_NEW_CARD_CAP - newReviewedToday);

  const out = [];
  for (let i = 0; i < due.length && out.length < cap; i++) out.push(due[i].card);
  for (let i = 0; i < fresh.length && out.length < cap; i++) out.push(fresh[i]);

  return {
    cards: out.map(function (c) {
      return { cardId: c.cardId, subject: c.subject, section: c.section || '', front: c.front, back: c.back, mediaType: c.mediaType || '', mediaDriveId: c.mediaDriveId || '' };
    }),
    dueCount: due.length,
    newAvailable: Math.min(fresh.length, newBudget)
  };
}

/**
 * Record a review and advance SRS state. Returns the updated state.
 */
function submitReview(token, cardId, rating) {
  const claims = requireAuth(token);
  if (!cardId) throw new Error('cardId required.');
  const ratingNum = Number(rating);
  const validRatings = [SRS.RATING.HARD, SRS.RATING.MEDIUM, SRS.RATING.EASY];
  if (validRatings.indexOf(ratingNum) === -1) throw new Error('Invalid rating.');

  const existing = findWhere(SHEETS.STUDY_PROGRESS, function (r) {
    return r.userEmail === claims.email && r.cardId === cardId;
  })[0];

  const base = existing || { ef: SRS.DEFAULT_EF, interval: 0, reps: 0 };
  const next = srsUpdate_(base, ratingNum);

  upsertRow(SHEETS.STUDY_PROGRESS, ['userEmail', 'cardId'], [claims.email, cardId], {
    ef: next.ef,
    interval: next.interval,
    reps: next.reps,
    nextDue: next.nextDue,
    lastReviewed: next.lastReviewed
  });
  invalidateLeaderboard_();
  return next;
}

/**
 * Flag a flashcard for teacher review by setting column H to "Needs Review".
 */
function flagCard(token, cardId) {
  requireAuth(token);
  if (!cardId) throw new Error('cardId required.');
  const sh = sheet_(SHEETS.FLASHCARDS);
  const lastRow = sh.getLastRow();
  if (lastRow < 2) throw new Error('Card not found.');
  if (!sh.getRange(1, 8).getValue()) sh.getRange(1, 8).setValue('flag');
  const ids = sh.getRange(2, 1, lastRow - 1, 1).getValues();
  for (let i = 0; i < ids.length; i++) {
    if (String(ids[i][0]) === String(cardId)) {
      sh.getRange(i + 2, 8).setValue('Needs Review');
      invalidate_(SHEETS.FLASHCARDS);
      return;
    }
  }
  throw new Error('Card not found.');
}

/**
 * Summary stats for the dashboard: total cards reviewed, due today by subject.
 */
function getStudyStats(token) {
  const claims = requireAuth(token);
  const allCards = readAll(SHEETS.FLASHCARDS);
  const progress = findWhere(SHEETS.STUDY_PROGRESS, function (r) { return r.userEmail === claims.email; });
  const today = todayStartIso_();
  const todayMs = new Date(today).getTime();
  const msPerDay = 86400000;

  const subjectMeta = {};
  SUBJECTS.forEach(function (s) { subjectMeta[s] = { total: 0, startMs: Infinity }; });
  const cardToSubject = {};
  allCards.forEach(function (c) {
    cardToSubject[c.cardId] = c.subject;
    if (!subjectMeta[c.subject]) return;
    subjectMeta[c.subject].total += 1;
    const t = c.createdAt ? new Date(String(c.createdAt)).getTime() : todayMs;
    if (t < subjectMeta[c.subject].startMs) subjectMeta[c.subject].startMs = t;
  });

  const bySubject = {};
  SUBJECTS.forEach(function (s) { bySubject[s] = { known: 0, srsDue: 0 }; });
  progress.forEach(function (p) {
    const subj = cardToSubject[p.cardId];
    if (!subj || !bySubject[subj]) return;
    bySubject[subj].known += 1;
    if (p.nextDue && String(p.nextDue) <= today) bySubject[subj].srsDue += 1;
  });

  SUBJECTS.forEach(function (s) {
    const meta = subjectMeta[s];
    const bs = bySubject[s];
    const daysElapsed = meta.startMs === Infinity ? 1 : Math.floor((todayMs - meta.startMs) / msPerDay) + 1;
    const scheduledSoFar = Math.min(meta.total, daysElapsed * SRS.DAILY_NEW_CARD_CAP);
    const scheduledDue = Math.max(0, scheduledSoFar - bs.known);
    bs.total = meta.total;
    bs.pending = Math.min(100, bs.srsDue + scheduledDue);
  });

  return { bySubject: bySubject, subjects: SUBJECTS };
}
