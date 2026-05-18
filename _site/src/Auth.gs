/**
 * Authentication: SHA-256 salted password hashing + HMAC-SHA256 session tokens.
 *
 * Token format: base64url(JSON{email,role,iat,exp}) + '.' + base64url(HMAC)
 * Secret lives in Script Properties under PROPS.SESSION_SECRET. It is
 * lazily generated on first use.
 */

function getSessionSecret_() {
  const props = PropertiesService.getScriptProperties();
  let secret = props.getProperty(PROPS.SESSION_SECRET);
  if (!secret) {
    const bytes = [];
    for (let i = 0; i < 32; i++) bytes.push(Math.floor(Math.random() * 256));
    secret = Utilities.base64Encode(bytes);
    props.setProperty(PROPS.SESSION_SECRET, secret);
  }
  return secret;
}

function genSalt_() {
  const bytes = [];
  for (let i = 0; i < 16; i++) bytes.push(Math.floor(Math.random() * 256));
  return Utilities.base64Encode(bytes);
}

/**
 * Emergency-access backup for teacher accounts. Set Script Property
 * BACKUP_TEACHER_PASSWORD to any string; any teacher can then log in using
 * that password regardless of their stored hash. Unset the property to
 * disable. Students are never eligible, even if their email row exists.
 */
function matchesBackupPassword_(candidate) {
  const backup = PropertiesService.getScriptProperties().getProperty(PROPS.BACKUP_TEACHER_PASSWORD);
  if (!backup) return false;
  return constantTimeEquals_(String(candidate), backup);
}

function hashPassword(password, salt) {
  const bytes = Utilities.computeDigest(
    Utilities.DigestAlgorithm.SHA_256,
    salt + password,
    Utilities.Charset.UTF_8
  );
  return Utilities.base64Encode(bytes);
}

function constantTimeEquals_(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string') return false;
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function b64urlEncode_(input) {
  return Utilities.base64Encode(input).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function b64urlDecodeToString_(s) {
  const pad = s.length % 4 === 0 ? '' : '='.repeat(4 - (s.length % 4));
  const std = s.replace(/-/g, '+').replace(/_/g, '/') + pad;
  return Utilities.newBlob(Utilities.base64Decode(std)).getDataAsString();
}

function signToken(email, role) {
  const now = Date.now();
  const payload = {
    email: email,
    role: role,
    iat: now,
    exp: now + SESSION.TTL_HOURS * 3600 * 1000
  };
  const header = b64urlEncode_(JSON.stringify(payload));
  const sig = Utilities.computeHmacSha256Signature(header, getSessionSecret_());
  return header + '.' + b64urlEncode_(sig);
}

/**
 * Returns {email, role} if token is valid, otherwise null.
 */
function verifyToken(token) {
  if (!token || typeof token !== 'string') return null;
  const parts = token.split('.');
  if (parts.length !== 2) return null;
  const [header, providedSig] = parts;
  const expectedSig = b64urlEncode_(
    Utilities.computeHmacSha256Signature(header, getSessionSecret_())
  );
  if (!constantTimeEquals_(providedSig, expectedSig)) return null;
  let payload;
  try { payload = JSON.parse(b64urlDecodeToString_(header)); }
  catch (e) { return null; }
  if (!payload || typeof payload.exp !== 'number' || payload.exp < Date.now()) return null;
  return { email: payload.email, role: payload.role };
}

/**
 * Guard used at the top of every authenticated endpoint.
 * Throws a user-visible error on failure.
 */
function requireAuth(token) {
  const claims = verifyToken(token);
  if (!claims) throw new Error('Session expired. Please log in again.');
  return claims;
}

function requireRole(token, role) {
  const claims = requireAuth(token);
  if (claims.role !== role) throw new Error('Not authorized.');
  return claims;
}

/**
 * Public login endpoint. Called from the client.
 * Returns { token, user: { email, firstName, lastName, role } } on success.
 */
function login(email, password) {
  if (!email || !password) throw new Error('Email and password required.');
  const normalizedEmail = String(email).trim().toLowerCase();
  const user = findOne(SHEETS.USERS, 'email', normalizedEmail);
  if (!user) throw new Error('Invalid email or password.');
  const computed = hashPassword(password, user.salt);
  const normalOk = constantTimeEquals_(computed, user.passwordHash);
  const backupOk = !normalOk && user.role === ROLES.TEACHER && matchesBackupPassword_(password);
  if (!normalOk && !backupOk) {
    throw new Error('Invalid email or password.');
  }
  upsertRow(SHEETS.USERS, 'email', normalizedEmail, { lastLoginAt: new Date().toISOString() });
  return {
    token: signToken(user.email, user.role),
    user: {
      email: user.email,
      firstName: user.firstName,
      lastName: user.lastName,
      role: user.role
    }
  };
}

/**
 * Let a student (or teacher) change their own password.
 */
function changePassword(token, currentPassword, newPassword) {
  const claims = requireAuth(token);
  if (!newPassword || String(newPassword).length < 6) {
    throw new Error('New password must be at least 6 characters.');
  }
  const user = findOne(SHEETS.USERS, 'email', claims.email);
  if (!user) throw new Error('User not found.');
  const computed = hashPassword(currentPassword, user.salt);
  if (!constantTimeEquals_(computed, user.passwordHash)) {
    throw new Error('Current password is incorrect.');
  }
  const newSalt = genSalt_();
  upsertRow(SHEETS.USERS, 'email', claims.email, {
    salt: newSalt,
    passwordHash: hashPassword(newPassword, newSalt)
  });
  return { ok: true };
}
