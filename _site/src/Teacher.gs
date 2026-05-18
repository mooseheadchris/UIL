/**
 * Teacher-only endpoints. Every function guards on requireRole(token, 'teacher').
 */

function teacher_listUsers(token) {
  requireRole(token, ROLES.TEACHER);
  return readAll(SHEETS.USERS).map(function (u) {
    return {
      email: u.email,
      role: u.role,
      firstName: u.firstName,
      lastName: u.lastName,
      createdAt: u.createdAt,
      lastLoginAt: u.lastLoginAt
    };
  });
}

function teacher_importRoster(token, csvText) {
  requireRole(token, ROLES.TEACHER);
  return importRoster_(csvText);
}

function teacher_resetPassword(token, email) {
  requireRole(token, ROLES.TEACHER);
  const user = getUserByEmail_(email);
  if (!user) throw new Error('User not found.');
  const temp = genTempPassword_();
  const salt = genSalt_();
  upsertRow(SHEETS.USERS, 'email', normalizeEmail_(email), {
    salt: salt,
    passwordHash: hashPassword(temp, salt)
  });
  return { email: user.email, tempPassword: temp };
}

function teacher_createUser(token, fields) {
  requireRole(token, ROLES.TEACHER);
  return createUser_(fields);
}

/**
 * Parse a CSV with a required header row into objects keyed by lowercased
 * header names. Trailing/leading whitespace in headers is trimmed.
 * Returns { header: [string], rows: [{col: value, ...}] }.
 */
function parseCsvWithHeader_(csvText) {
  const lines = String(csvText).split(/\r?\n/).map(function (l) { return l.trim(); }).filter(Boolean);
  if (!lines.length) return { header: [], rows: [] };
  const tsv = lines[0].indexOf('\t') !== -1;
  function splitLine(line) { return tsv ? line.split('\t').map(function (s) { return s.trim(); }) : splitCsvLine_(line); }
  const header = splitLine(lines[0]).map(function (s) { return s.toLowerCase(); });
  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    const cols = splitLine(lines[i]);
    const row = { _lineNum: i + 1 };
    header.forEach(function (h, idx) { row[h] = cols[idx] != null ? cols[idx] : ''; });
    rows.push(row);
  }
  return { header: header, rows: rows };
}

/**
 * CSV header row required. Columns: subject, section (optional), front, back.
 * `section` may be omitted entirely or left blank on any row.
 */
function teacher_uploadFlashcards(token, csvText) {
  const claims = requireRole(token, ROLES.TEACHER);
  const parsed = parseCsvWithHeader_(csvText);
  if (!parsed.header.length) return { created: 0, errors: ['CSV is empty.'] };
  if (parsed.header.indexOf('subject') === -1 || parsed.header.indexOf('front') === -1 || parsed.header.indexOf('back') === -1) {
    return { created: 0, errors: ['CSV must have a header row with subject, front, back (section optional).'] };
  }

  const now = new Date().toISOString();
  const rows = [];
  const errors = [];
  parsed.rows.forEach(function (r) {
    const subject = r.subject;
    const section = (r.section || '').trim();
    const front = r.front;
    const back = r.back;
    if (!subject || !front || !back) { errors.push('Line ' + r._lineNum + ': missing required fields'); return; }
    if (SUBJECTS.indexOf(subject) === -1) { errors.push('Line ' + r._lineNum + ': unknown subject "' + subject + '"'); return; }
    rows.push({
      cardId: genId('card'),
      subject: subject,
      section: section,
      front: front,
      back: back,
      createdAt: now,
      createdBy: claims.email
    });
  });
  if (rows.length) appendRows(SHEETS.FLASHCARDS, rows);
  return { created: rows.length, errors: errors };
}

/**
 * Create a single flashcard with optional media (image or audio).
 * mediaBase64 is the raw Base64 string (no data-URL prefix).
 */
function teacher_addFlashcardWithMedia(token, subject, section, front, back, mediaType, mediaBase64, mediaFilename, mediaMimeType) {
  const claims = requireRole(token, ROLES.TEACHER);
  if (!subject || SUBJECTS.indexOf(subject) === -1) throw new Error('Invalid subject.');
  if (!front) throw new Error('front required.');
  if (!back) throw new Error('back required.');

  let resolvedMediaType = '';
  let mediaDriveId = '';
  if (mediaType && mediaBase64 && mediaFilename) {
    const folder = getMediaFolder_();
    const blob = Utilities.newBlob(Utilities.base64Decode(mediaBase64), mediaMimeType || 'application/octet-stream', mediaFilename);
    const file = folder.createFile(blob);
    file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    mediaDriveId = file.getId();
    resolvedMediaType = mediaType;
  }

  const row = {
    cardId: genId('card'),
    subject: subject,
    section: section ? String(section).trim() : '',
    front: front,
    back: back,
    createdAt: new Date().toISOString(),
    createdBy: claims.email,
    mediaType: resolvedMediaType,
    mediaDriveId: mediaDriveId
  };
  appendRow(SHEETS.FLASHCARDS, row);
  return { cardId: row.cardId };
}

function getMediaFolder_() {
  const props = PropertiesService.getScriptProperties();
  const folderId = props.getProperty('MEDIA_FOLDER_ID');
  if (folderId) {
    try { return DriveApp.getFolderById(folderId); } catch (e) { /* fall through */ }
  }
  const folder = DriveApp.createFolder('AcDec Flashcard Media');
  props.setProperty('MEDIA_FOLDER_ID', folder.getId());
  return folder;
}

/**
 * CSV header row required. Columns: subject, section (optional), prompt,
 * choiceA, choiceB, choiceC, choiceD, correctChoice, explanation (optional).
 */
function teacher_uploadQuestions(token, csvText) {
  const claims = requireRole(token, ROLES.TEACHER);
  const parsed = parseCsvWithHeader_(csvText);
  if (!parsed.header.length) return { created: 0, errors: ['CSV is empty.'] };
  const required = ['subject', 'prompt', 'choicea', 'choiceb', 'choicec', 'choiced', 'correctchoice'];
  for (let i = 0; i < required.length; i++) {
    if (parsed.header.indexOf(required[i]) === -1) {
      return { created: 0, errors: ['CSV header must include: ' + required.join(', ') + ' (explanation and section are optional).'] };
    }
  }

  const now = new Date().toISOString();
  const rows = [];
  const errors = [];
  parsed.rows.forEach(function (r) {
    const subject = r.subject;
    const section = (r.section || '').trim();
    const prompt = r.prompt;
    const a = r.choicea, b = r.choiceb, c = r.choicec, d = r.choiced;
    const correct = String(r.correctchoice || '').trim().toUpperCase();
    const explanation = r.explanation || '';
    if (!subject || !prompt || !a || !b || !c || !d) { errors.push('Line ' + r._lineNum + ': missing required fields'); return; }
    if (SUBJECTS.indexOf(subject) === -1) { errors.push('Line ' + r._lineNum + ': unknown subject "' + subject + '"'); return; }
    if (['A', 'B', 'C', 'D'].indexOf(correct) === -1) { errors.push('Line ' + r._lineNum + ': correctChoice must be A/B/C/D'); return; }
    rows.push({
      questionId: genId('q'),
      subject: subject,
      section: section,
      prompt: prompt,
      choiceA: a,
      choiceB: b,
      choiceC: c,
      choiceD: d,
      correctChoice: correct,
      explanation: explanation,
      createdAt: now,
      createdBy: claims.email
    });
  });
  if (rows.length) appendRows(SHEETS.QUESTIONS, rows);
  return { created: rows.length, errors: errors };
}

function teacher_contentCounts(token) {
  requireRole(token, ROLES.TEACHER);
  const cards = readAll(SHEETS.FLASHCARDS);
  const questions = readAll(SHEETS.QUESTIONS);
  const out = {};
  SUBJECTS.forEach(function (s) { out[s] = { flashcards: 0, questions: 0 }; });
  cards.forEach(function (c) { if (out[c.subject]) out[c.subject].flashcards += 1; });
  questions.forEach(function (q) { if (out[q.subject]) out[q.subject].questions += 1; });
  return out;
}

/**
 * Per-student participation report.
 */
function teacher_studentReport(token) {
  requireRole(token, ROLES.TEACHER);
  const students = readAll(SHEETS.USERS).filter(function (u) { return u.role === ROLES.STUDENT; });
  const progress = readAll(SHEETS.STUDY_PROGRESS);
  const attempts = readAll(SHEETS.QUIZ_ATTEMPTS);

  const reviewsByEmail = {};
  const lastActiveByEmail = {};
  progress.forEach(function (p) {
    reviewsByEmail[p.userEmail] = (reviewsByEmail[p.userEmail] || 0) + (Number(p.reps) || 0);
    if (p.lastReviewed && (!lastActiveByEmail[p.userEmail] || p.lastReviewed > lastActiveByEmail[p.userEmail])) {
      lastActiveByEmail[p.userEmail] = p.lastReviewed;
    }
  });

  const quizStatsByEmail = {};
  attempts.forEach(function (a) {
    const s = quizStatsByEmail[a.userEmail] || { attempts: 0, totalScore: 0, totalQuestions: 0 };
    s.attempts += 1;
    s.totalScore += Number(a.score) || 0;
    s.totalQuestions += Number(a.totalQuestions) || 0;
    quizStatsByEmail[a.userEmail] = s;
    if (a.completedAt && (!lastActiveByEmail[a.userEmail] || a.completedAt > lastActiveByEmail[a.userEmail])) {
      lastActiveByEmail[a.userEmail] = a.completedAt;
    }
  });

  return students.map(function (u) {
    const qs = quizStatsByEmail[u.email] || { attempts: 0, totalScore: 0, totalQuestions: 0 };
    const avg = qs.totalQuestions > 0 ? Math.round(100 * qs.totalScore / qs.totalQuestions) : null;
    return {
      email: u.email,
      name: ((u.firstName || '') + ' ' + (u.lastName || '')).trim(),
      cardsReviewed: reviewsByEmail[u.email] || 0,
      quizAttempts: qs.attempts,
      quizAvgPct: avg,
      lastActiveAt: lastActiveByEmail[u.email] || ''
    };
  });
}

function teacher_subjectReport(token) {
  requireRole(token, ROLES.TEACHER);
  const attempts = readAll(SHEETS.QUIZ_ATTEMPTS);
  const out = {};
  SUBJECTS.forEach(function (s) { out[s] = { attempts: 0, totalScore: 0, totalQuestions: 0 }; });
  attempts.forEach(function (a) {
    const s = out[a.subject];
    if (!s) return;
    s.attempts += 1;
    s.totalScore += Number(a.score) || 0;
    s.totalQuestions += Number(a.totalQuestions) || 0;
  });
  return SUBJECTS.map(function (subj) {
    const s = out[subj];
    return {
      subject: subj,
      attempts: s.attempts,
      avgPct: s.totalQuestions > 0 ? Math.round(100 * s.totalScore / s.totalQuestions) : null
    };
  });
}

// ---------------------------------------------------------------------------
// Content management (edit + delete) — teacher-only.
// Shared filter shape for list endpoints:
//   { subject?: string, section?: string, search?: string, page?: number, pageSize?: number }
// Returns: { rows, total, page, pageSize }.
// ---------------------------------------------------------------------------

function paginate_(rows, opts) {
  const page = Math.max(1, Number(opts && opts.page) || 1);
  const pageSize = Math.min(100, Math.max(1, Number(opts && opts.pageSize) || 25));
  const start = (page - 1) * pageSize;
  return { rows: rows.slice(start, start + pageSize), total: rows.length, page: page, pageSize: pageSize };
}

function applyContentFilters_(rows, opts, searchFields) {
  const o = opts || {};
  const subject = o.subject || null;
  const section = o.section || null; // exact match; '' means "no filter" here since students/UI never submit blank-as-filter
  const search = String(o.search || '').toLowerCase().trim();
  let filtered = rows;
  if (subject) filtered = filtered.filter(function (r) { return r.subject === subject; });
  if (section) filtered = filtered.filter(function (r) { return String(r.section || '').trim() === section; });
  if (search) filtered = filtered.filter(function (r) {
    const hay = searchFields.map(function (f) { return String(r[f] || ''); }).join(' ').toLowerCase();
    return hay.indexOf(search) !== -1;
  });
  filtered.sort(function (a, b) { return String(b.createdAt).localeCompare(String(a.createdAt)); });
  return filtered;
}

function teacher_listFlashcards(token, opts) {
  requireRole(token, ROLES.TEACHER);
  const filtered = applyContentFilters_(readAll(SHEETS.FLASHCARDS), opts, ['front', 'back']);
  return paginate_(filtered, opts);
}

function teacher_updateFlashcard(token, cardId, updates) {
  requireRole(token, ROLES.TEACHER);
  if (!cardId) throw new Error('cardId required.');
  if (!findOne(SHEETS.FLASHCARDS, 'cardId', cardId)) throw new Error('Flashcard not found.');
  const allowed = ['subject', 'section', 'front', 'back'];
  const clean = {};
  allowed.forEach(function (k) { if (updates && updates[k] !== undefined) clean[k] = String(updates[k]); });
  if (clean.subject && SUBJECTS.indexOf(clean.subject) === -1) throw new Error('Unknown subject: ' + clean.subject);
  if (clean.section !== undefined) clean.section = String(clean.section).trim();
  if (clean.front !== undefined && !clean.front) throw new Error('Front cannot be blank.');
  if (clean.back !== undefined && !clean.back) throw new Error('Back cannot be blank.');
  upsertRow(SHEETS.FLASHCARDS, 'cardId', cardId, clean);
  return { ok: true };
}

function teacher_deleteFlashcard(token, cardId) {
  requireRole(token, ROLES.TEACHER);
  if (!cardId) throw new Error('cardId required.');
  const removed = deleteRowByKey(SHEETS.FLASHCARDS, 'cardId', cardId);
  if (!removed) throw new Error('Flashcard not found.');
  deleteRowsByKey(SHEETS.STUDY_PROGRESS, 'cardId', cardId);
  invalidateLeaderboard_();
  return { ok: true };
}

function teacher_listQuestions(token, opts) {
  requireRole(token, ROLES.TEACHER);
  const filtered = applyContentFilters_(readAll(SHEETS.QUESTIONS), opts, ['prompt', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'explanation']);
  return paginate_(filtered, opts);
}

function teacher_updateQuestion(token, questionId, updates) {
  requireRole(token, ROLES.TEACHER);
  if (!questionId) throw new Error('questionId required.');
  if (!findOne(SHEETS.QUESTIONS, 'questionId', questionId)) throw new Error('Question not found.');
  const allowed = ['subject', 'section', 'prompt', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'correctChoice', 'explanation'];
  const clean = {};
  allowed.forEach(function (k) { if (updates && updates[k] !== undefined) clean[k] = String(updates[k]); });
  if (clean.subject && SUBJECTS.indexOf(clean.subject) === -1) throw new Error('Unknown subject: ' + clean.subject);
  if (clean.section !== undefined) clean.section = String(clean.section).trim();
  if (clean.correctChoice !== undefined) {
    const c = String(clean.correctChoice).trim().toUpperCase();
    if (['A', 'B', 'C', 'D'].indexOf(c) === -1) throw new Error('correctChoice must be A/B/C/D.');
    clean.correctChoice = c;
  }
  ['prompt', 'choiceA', 'choiceB', 'choiceC', 'choiceD'].forEach(function (k) {
    if (clean[k] !== undefined && !clean[k]) throw new Error(k + ' cannot be blank.');
  });
  upsertRow(SHEETS.QUESTIONS, 'questionId', questionId, clean);
  return { ok: true };
}

function teacher_deleteQuestion(token, questionId) {
  requireRole(token, ROLES.TEACHER);
  if (!questionId) throw new Error('questionId required.');
  const removed = deleteRowByKey(SHEETS.QUESTIONS, 'questionId', questionId);
  if (!removed) throw new Error('Question not found.');
  // We keep QuizAnswers / QuizAttempts rows so historical scores stay intact.
  return { ok: true };
}

/**
 * All non-blank sections present for a given subject + content type, for
 * populating teacher-side filter dropdowns.
 * Avoids delegating to listSections() to prevent a redundant requireAuth
 * call (requireRole above already verified the token).
 */
function teacher_listSections(token, subject, contentType) {
  requireRole(token, ROLES.TEACHER);
  const sheet = contentType === 'questions' ? SHEETS.QUESTIONS : SHEETS.FLASHCARDS;
  const subj = subject || null;
  const set = {};
  readAll(sheet).forEach(function (r) {
    if (subj && r.subject !== subj) return;
    const s = String(r.section || '').trim();
    if (s) set[s] = true;
  });
  return Object.keys(set).sort();
}

/**
 * Force-set nextDue to targetDate (ISO date string, defaults to today) on all
 * StudyProgress rows for cards matching subject / section. Students who have
 * never touched a card are unaffected — those cards surface as fresh anyway.
 */
function teacher_setCardsDue(token, subject, section, targetDate) {
  requireRole(token, ROLES.TEACHER);
  if (!subject || SUBJECTS.indexOf(subject) === -1) throw new Error('Invalid subject.');

  const sectionSel = section ? String(section).trim() : null;
  const cardIds = {};
  readAll(SHEETS.FLASHCARDS).forEach(function (c) {
    if (c.subject !== subject) return;
    if (sectionSel && String(c.section || '').trim() !== sectionSel) return;
    cardIds[c.cardId] = true;
  });
  if (!Object.keys(cardIds).length) throw new Error('No cards found for that subject/section.');

  const dueIso = targetDate ? String(targetDate) : todayStartIso_();

  const sh = sheet_(SHEETS.STUDY_PROGRESS);
  const header = SCHEMA[SHEETS.STUDY_PROGRESS];
  const lastRow = sh.getLastRow();
  if (lastRow < 2) return { updated: 0 };

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const values = sh.getRange(2, 1, lastRow - 1, header.length).getValues();
    const cardIdIdx = header.indexOf('cardId');
    const nextDueIdx = header.indexOf('nextDue');
    let updated = 0;
    for (let i = 0; i < values.length; i++) {
      if (cardIds[values[i][cardIdIdx]]) {
        values[i][nextDueIdx] = dueIso;
        updated++;
      }
    }
    if (updated > 0) {
      sh.getRange(2, 1, values.length, header.length).setValues(values);
      invalidate_(SHEETS.STUDY_PROGRESS);
    }
    return { updated: updated };
  } finally {
    lock.releaseLock();
  }
}
