/**
 * Web app entry points and one-time setup helpers.
 *
 * doGet()            — serves the SPA shell.
 * include(name)      — template helper for pulling partial .html files.
 * setupSpreadsheet() — run once from the editor: creates all tabs + seeds
 *                      an initial teacher account you can log in with.
 */

function doGet(e) {
  const tpl = HtmlService.createTemplateFromFile('html/index');
  tpl.subjects = SUBJECTS;
  return tpl.evaluate()
    .setTitle('AcDec Study')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * Template include helper. Use in .html files as:
 *   <?!= include('html/styles') ?>
 */
function include(path) {
  return HtmlService.createHtmlOutputFromFile(path).getContent();
}

/**
 * Returns client bootstrap info. Called from index.html on load.
 */
function bootstrap() {
  return {
    subjects: SUBJECTS,
    srs: { defaultSessionSize: SRS.DEFAULT_SESSION_SIZE, dailyNewCap: SRS.DAILY_NEW_CARD_CAP }
  };
}

/**
 * Return non-blank section names for a given subject + content type.
 * Students call this to populate the section picker in Study/Quiz.
 *   contentType: 'flashcards' | 'questions'
 *   subject: exact SUBJECTS entry, or '' / null for all subjects
 */
function listSections(token, subject, contentType) {
  requireAuth(token);
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
 * One-time setup. Run manually from the Apps Script editor.
 *
 * Creates all required sheets/headers and (if no teacher exists yet) seeds
 * a teacher account. Logs the temporary password to the editor log and
 * also stores it in a Script Property called SEED_TEACHER_PASSWORD so you
 * can retrieve it later from Project Settings → Script Properties.
 *
 * After first run, CHANGE the seed teacher's password from the teacher UI,
 * then delete SEED_TEACHER_PASSWORD from Script Properties.
 */
function setupSpreadsheet() {
  ensureSheets();

  const existingTeacher = readAll(SHEETS.USERS).filter(function (u) {
    return u.role === ROLES.TEACHER;
  })[0];
  if (existingTeacher) {
    Logger.log('Setup complete. Existing teacher: %s', existingTeacher.email);
    return;
  }

  const seedEmail = Session.getActiveUser().getEmail() || 'teacher@example.com';
  const tempPassword = genTempPassword_();
  createUser_({
    email: seedEmail,
    firstName: 'Teacher',
    lastName: '',
    initialPassword: tempPassword,
    role: ROLES.TEACHER
  });
  PropertiesService.getScriptProperties().setProperty('SEED_TEACHER_PASSWORD', tempPassword);
  Logger.log('Seed teacher created:');
  Logger.log('  email: %s', seedEmail);
  Logger.log('  password: %s  (also in Script Properties as SEED_TEACHER_PASSWORD)', tempPassword);
  Logger.log('CHANGE IT after first login, then delete SEED_TEACHER_PASSWORD from Script Properties.');
}

/**
 * Utility for debugging: nuke non-user data. DO NOT expose via the web.
 * Keep Users so logins still work; clears all learning data.
 */
function devResetContent() {
  const ss = SpreadsheetApp.getActive();
  [SHEETS.FLASHCARDS, SHEETS.QUESTIONS, SHEETS.STUDY_PROGRESS, SHEETS.QUIZ_ATTEMPTS, SHEETS.QUIZ_ANSWERS].forEach(function (name) {
    const sheet = ss.getSheetByName(name);
    if (!sheet) return;
    const lastRow = sheet.getLastRow();
    if (lastRow > 1) sheet.getRange(2, 1, lastRow - 1, sheet.getLastColumn()).clearContent();
    invalidate_(name);
  });
  invalidateLeaderboard_();
}
