/**
 * Quiz lifecycle: start, serve questions without answers, score server-side.
 *
 * The full question set (including correct choices) for an active attempt is
 * kept in CacheService keyed by attemptId. Clients never see correct answers
 * until submission.
 */

function quizCacheKey_(attemptId) { return 'quiz:' + attemptId; }

function shuffle_(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const tmp = a[i]; a[i] = a[j]; a[j] = tmp;
  }
  return a;
}

/**
 * Start a quiz attempt. Returns the attemptId + sanitized questions.
 *
 * Section filter rules mirror Study:
 *   - falsy section → all matching-subject questions, blank section included.
 *   - specific section → exact match only; blank-section questions excluded.
 *
 * Sanitized question shape:
 *   { questionId, prompt, choices: { A, B, C, D } }
 */
function startQuiz(token, subject, section, questionCount) {
  const claims = requireAuth(token);
  if (SUBJECTS.indexOf(subject) === -1) throw new Error('Unknown subject: ' + subject);

  const sectionSel = section ? String(section).trim() : null;
  const pool = findWhere(SHEETS.QUESTIONS, function (q) {
    if (q.subject !== subject) return false;
    if (sectionSel && String(q.section || '').trim() !== sectionSel) return false;
    return true;
  });
  if (!pool.length) {
    const suffix = sectionSel ? ' (' + sectionSel + ')' : '';
    throw new Error('No questions available for ' + subject + suffix + ' yet.');
  }

  const n = Math.min(Math.max(Number(questionCount) || 10, 1), Math.min(50, pool.length));
  const picked = shuffle_(pool).slice(0, n);
  const attemptId = genId('attempt');

  const sanitized = picked.map(function (q) {
    return {
      questionId: q.questionId,
      prompt: q.prompt,
      choices: { A: q.choiceA, B: q.choiceB, C: q.choiceC, D: q.choiceD }
    };
  });

  const payload = {
    attemptId: attemptId,
    email: claims.email,
    subject: subject,
    startedAt: new Date().toISOString(),
    questions: picked.map(function (q) {
      return { questionId: q.questionId, correctChoice: q.correctChoice, explanation: q.explanation };
    })
  };
  cache_().put(quizCacheKey_(attemptId), JSON.stringify(payload), SESSION.QUIZ_CACHE_TTL_SEC);

  return { attemptId: attemptId, subject: subject, questions: sanitized };
}

/**
 * Submit answers. `answers` is { questionId: 'A'|'B'|'C'|'D', ... }
 * Scores server-side, writes QuizAttempts + QuizAnswers, returns breakdown.
 */
function submitQuiz(token, attemptId, answers) {
  const claims = requireAuth(token);
  if (!attemptId) throw new Error('attemptId required.');
  const cached = cache_().get(quizCacheKey_(attemptId));
  if (!cached) throw new Error('Quiz expired. Please start a new attempt.');
  const payload = JSON.parse(cached);
  if (payload.email !== claims.email) throw new Error('Attempt does not belong to this user.');

  const ans = answers || {};
  const completedAt = new Date().toISOString();
  let score = 0;
  const breakdown = [];
  const answerRows = [];

  payload.questions.forEach(function (q) {
    const chosen = String(ans[q.questionId] || '').toUpperCase();
    const isCorrect = chosen === String(q.correctChoice).toUpperCase();
    if (isCorrect) score += 1;
    breakdown.push({
      questionId: q.questionId,
      chosen: chosen || null,
      correct: q.correctChoice,
      isCorrect: isCorrect,
      explanation: q.explanation || ''
    });
    answerRows.push({
      attemptId: attemptId,
      questionId: q.questionId,
      chosen: chosen,
      isCorrect: isCorrect ? 'TRUE' : 'FALSE'
    });
  });

  appendRow(SHEETS.QUIZ_ATTEMPTS, {
    attemptId: attemptId,
    userEmail: claims.email,
    subject: payload.subject,
    startedAt: payload.startedAt,
    completedAt: completedAt,
    score: score,
    totalQuestions: payload.questions.length
  });
  appendRows(SHEETS.QUIZ_ANSWERS, answerRows);
  cache_().remove(quizCacheKey_(attemptId));
  invalidateLeaderboard_();

  return {
    score: score,
    total: payload.questions.length,
    subject: payload.subject,
    breakdown: breakdown
  };
}

/**
 * Per-student history. Used on the dashboard and in teacher reports.
 */
function getMyAttempts(token, limit) {
  const claims = requireAuth(token);
  const rows = findWhere(SHEETS.QUIZ_ATTEMPTS, function (r) {
    return r.userEmail === claims.email;
  });
  rows.sort(function (a, b) { return String(b.completedAt).localeCompare(String(a.completedAt)); });
  return rows.slice(0, Math.min(limit || 20, 100));
}
