/**
 * Roster management and user CRUD.
 * All teacher-only endpoints live in Teacher.gs; shared helpers here.
 */

function normalizeEmail_(email) {
  return String(email || '').trim().toLowerCase();
}

function getUserByEmail_(email) {
  return findOne(SHEETS.USERS, 'email', normalizeEmail_(email));
}

/**
 * Create one user. Returns the row that was written (minus secrets).
 * If a row with the same email already exists, throws.
 */
function createUser_(fields) {
  const email = normalizeEmail_(fields.email);
  if (!email) throw new Error('Email required.');
  if (getUserByEmail_(email)) throw new Error('User already exists: ' + email);

  const role = (fields.role === ROLES.TEACHER) ? ROLES.TEACHER : ROLES.STUDENT;
  const password = fields.initialPassword || fields.password;
  if (!password) throw new Error('Initial password required for ' + email);

  const salt = genSalt_();
  appendRow(SHEETS.USERS, {
    email: email,
    role: role,
    firstName: fields.firstName || '',
    lastName: fields.lastName || '',
    salt: salt,
    passwordHash: hashPassword(password, salt),
    createdAt: new Date().toISOString(),
    lastLoginAt: ''
  });
  return { email: email, role: role };
}

/**
 * Parse the simple, opinionated CSV format used by the teacher dashboard:
 *   email,firstName,lastName,initialPassword,role
 * Header row is optional. Returns an array of {email,firstName,lastName,initialPassword,role}.
 */
function parseRosterCsv_(csvText) {
  const lines = String(csvText).split(/\r?\n/).map(function (l) { return l.trim(); }).filter(Boolean);
  if (!lines.length) return [];
  const rows = [];
  let startIdx = 0;
  const firstCols = lines[0].split(',').map(function (c) { return c.trim().toLowerCase(); });
  if (firstCols.indexOf('email') !== -1) startIdx = 1;
  for (let i = startIdx; i < lines.length; i++) {
    const cols = splitCsvLine_(lines[i]);
    if (!cols.length || !cols[0]) continue;
    rows.push({
      email: cols[0] || '',
      firstName: cols[1] || '',
      lastName: cols[2] || '',
      initialPassword: cols[3] || '',
      role: (cols[4] || '').toLowerCase() === 'teacher' ? ROLES.TEACHER : ROLES.STUDENT
    });
  }
  return rows;
}

/**
 * CSV splitter that honors double-quoted fields containing commas.
 */
function splitCsvLine_(line) {
  const out = [];
  let cur = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line.charAt(i);
    if (inQuotes) {
      if (c === '"' && line.charAt(i + 1) === '"') { cur += '"'; i++; }
      else if (c === '"') { inQuotes = false; }
      else { cur += c; }
    } else {
      if (c === ',') { out.push(cur); cur = ''; }
      else if (c === '"') { inQuotes = true; }
      else { cur += c; }
    }
  }
  out.push(cur);
  return out.map(function (s) { return s.trim(); });
}

/**
 * Bulk import roster. Skips rows for existing emails (reports them as skipped).
 * Returns { created: N, skipped: [emails] }.
 */
function importRoster_(csvText) {
  const rows = parseRosterCsv_(csvText);
  const created = [];
  const skipped = [];
  rows.forEach(function (r) {
    const email = normalizeEmail_(r.email);
    if (!email || !r.initialPassword) { skipped.push(email || '(blank)'); return; }
    if (getUserByEmail_(email)) { skipped.push(email); return; }
    const salt = genSalt_();
    created.push({
      email: email,
      role: r.role,
      firstName: r.firstName,
      lastName: r.lastName,
      salt: salt,
      passwordHash: hashPassword(r.initialPassword, salt),
      createdAt: new Date().toISOString(),
      lastLoginAt: ''
    });
  });
  if (created.length) appendRows(SHEETS.USERS, created);
  return { created: created.length, skipped: skipped };
}

/**
 * Generate a short human-readable temp password.
 */
function genTempPassword_() {
  const alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // no I,O,0,1
  let out = '';
  for (let i = 0; i < 10; i++) out += alphabet.charAt(Math.floor(Math.random() * alphabet.length));
  return out;
}
