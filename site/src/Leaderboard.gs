/**
 * Leaderboard aggregation, with 5-minute CacheService memoization.
 *
 * Points:
 *   - +1 per flashcard review (StudyProgress.reps rolls up; we count
 *     each row's reps for all-time; weekly uses lastReviewed).
 *   - +2 per correct quiz answer (QuizAnswers where isCorrect=TRUE).
 *
 * Per-student display: firstName + last-initial to avoid shoulder-surfing.
 */

function leaderboardCacheKey_(window) { return 'leaderboard:' + window; }

function invalidateLeaderboard_() {
  cache_().remove(leaderboardCacheKey_('all'));
  cache_().remove(leaderboardCacheKey_('7d'));
}

/**
 * window: 'all' | '7d'
 */
function getLeaderboard(token, window) {
  requireAuth(token);
  const w = window === '7d' ? '7d' : 'all';
  const cached = cache_().get(leaderboardCacheKey_(w));
  if (cached) {
    try { return JSON.parse(cached); } catch (e) { /* fall through */ }
  }

  const cutoff = w === '7d'
    ? new Date(Date.now() - 7 * 24 * 3600 * 1000).toISOString()
    : null;

  const users = readAll(SHEETS.USERS).filter(function (u) { return u.role === ROLES.STUDENT; });
  const scoreByEmail = {};
  users.forEach(function (u) {
    scoreByEmail[u.email] = {
      email: u.email,
      displayName: (u.firstName || '') + ' ' + (u.lastName ? u.lastName.charAt(0) + '.' : ''),
      reviews: 0,
      correctAnswers: 0,
      points: 0
    };
  });

  // Flashcard reviews.
  if (w === 'all') {
    readAll(SHEETS.STUDY_PROGRESS).forEach(function (p) {
      const entry = scoreByEmail[p.userEmail];
      if (!entry) return;
      const reps = Number(p.reps) || 0;
      entry.reviews += reps;
      entry.points += reps * POINTS.FLASHCARD_REVIEW;
    });
  } else {
    // Weekly: one point per card that was reviewed in the window.
    readAll(SHEETS.STUDY_PROGRESS).forEach(function (p) {
      const entry = scoreByEmail[p.userEmail];
      if (!entry || !p.lastReviewed || String(p.lastReviewed) < cutoff) return;
      entry.reviews += 1;
      entry.points += POINTS.FLASHCARD_REVIEW;
    });
  }

  // Quiz correct answers. We need attemptId → userEmail & completedAt.
  const attempts = readAll(SHEETS.QUIZ_ATTEMPTS);
  const attemptMeta = {};
  attempts.forEach(function (a) {
    attemptMeta[a.attemptId] = { email: a.userEmail, at: a.completedAt };
  });

  readAll(SHEETS.QUIZ_ANSWERS).forEach(function (row) {
    if (String(row.isCorrect).toUpperCase() !== 'TRUE') return;
    const meta = attemptMeta[row.attemptId];
    if (!meta) return;
    const entry = scoreByEmail[meta.email];
    if (!entry) return;
    if (cutoff && String(meta.at) < cutoff) return;
    entry.correctAnswers += 1;
    entry.points += POINTS.QUIZ_CORRECT;
  });

  const list = Object.keys(scoreByEmail).map(function (k) { return scoreByEmail[k]; })
    .filter(function (e) { return e.points > 0; })
    .sort(function (a, b) { return b.points - a.points; })
    .slice(0, 20)
    .map(function (e, i) {
      return {
        rank: i + 1,
        displayName: e.displayName,
        points: e.points,
        reviews: e.reviews,
        correctAnswers: e.correctAnswers
      };
    });

  const result = { window: w, entries: list, generatedAt: new Date().toISOString() };
  try {
    cache_().put(leaderboardCacheKey_(w), JSON.stringify(result), SESSION.LEADERBOARD_CACHE_TTL_SEC);
  } catch (e) { /* oversize: skip cache */ }
  return result;
}
