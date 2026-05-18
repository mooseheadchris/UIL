/**
 * Shared constants. Keep everything that might need to be tuned in one place.
 */

const SHEETS = {
  USERS: 'Users',
  FLASHCARDS: 'Flashcards',
  QUESTIONS: 'Questions',
  STUDY_PROGRESS: 'StudyProgress',
  QUIZ_ATTEMPTS: 'QuizAttempts',
  QUIZ_ANSWERS: 'QuizAnswers'
};

const SCHEMA = {
  Users: ['email', 'role', 'firstName', 'lastName', 'salt', 'passwordHash', 'createdAt', 'lastLoginAt'],
  Flashcards: ['cardId', 'subject', 'section', 'front', 'back', 'createdAt', 'createdBy', 'mediaType', 'mediaDriveId'],
  Questions: ['questionId', 'subject', 'section', 'prompt', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'choiceE', 'correctChoice', 'answerType', 'explanation', 'createdAt', 'createdBy'],
  StudyProgress: ['userEmail', 'cardId', 'ef', 'interval', 'reps', 'nextDue', 'lastReviewed'],
  QuizAttempts: ['attemptId', 'userEmail', 'subject', 'startedAt', 'completedAt', 'score', 'totalQuestions'],
  QuizAnswers: ['attemptId', 'questionId', 'chosen', 'isCorrect']
};

const ROLES = { STUDENT: 'student', TEACHER: 'teacher' };

const SUBJECTS = [
  'Number Sense',
  'Calculator',
  'Science',
  'Mathematics',
  'Computer Science',
];

const SRS = {
  DEFAULT_EF: 2.5,
  MIN_EF: 1.3,
  DAILY_NEW_CARD_CAP: 20,
  DEFAULT_SESSION_SIZE: 20,
  RATING: { HARD: 2, MEDIUM: 3, EASY: 5 }
};

const POINTS = {
  FLASHCARD_REVIEW: 1,
  QUIZ_CORRECT: 2
};

const SESSION = {
  TTL_HOURS: 12,
  QUIZ_CACHE_TTL_SEC: 30 * 60,
  LEADERBOARD_CACHE_TTL_SEC: 5 * 60
};

const PROPS = {
  SESSION_SECRET: 'SESSION_SECRET',
  BACKUP_TEACHER_PASSWORD: 'BACKUP_TEACHER_PASSWORD'
};
