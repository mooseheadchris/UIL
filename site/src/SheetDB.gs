/**
 * Low-level sheet access + per-sheet caching + write serialization.
 * Every other module should go through these helpers.
 *
 * Conventions:
 *   - Row 1 of every sheet is the header matching SCHEMA[sheetName].
 *   - Dates are stored as ISO strings so they round-trip via JSON.
 *   - readAll() caches the full sheet in CacheService under "db:<sheetName>".
 *   - Any write (append/update/delete) invalidates that cache key.
 */

function db_() { return SpreadsheetApp.getActive(); }

function sheet_(name) {
  const s = db_().getSheetByName(name);
  if (!s) throw new Error('Missing sheet: ' + name);
  return s;
}

function cache_() { return CacheService.getScriptCache(); }

function cacheKey_(sheetName) { return 'db:' + sheetName; }

function invalidate_(sheetName) {
  cache_().remove(cacheKey_(sheetName));
}

/**
 * Returns all rows as objects keyed by header. Cached for 30s; mutations
 * invalidate the key so within-request consistency is fine.
 */
function readAll(sheetName) {
  const cached = cache_().get(cacheKey_(sheetName));
  if (cached) {
    try { return JSON.parse(cached); } catch (e) { /* fall through */ }
  }
  const sheet = sheet_(sheetName);
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();
  if (lastRow < 2) return [];
  const values = sheet.getRange(1, 1, lastRow, lastCol).getValues();
  const header = values[0];
  const rows = [];
  for (let i = 1; i < values.length; i++) {
    const obj = {};
    for (let j = 0; j < header.length; j++) {
      const v = values[i][j];
      obj[header[j]] = v instanceof Date ? v.toISOString() : v;
    }
    rows.push(obj);
  }
  try {
    cache_().put(cacheKey_(sheetName), JSON.stringify(rows), 30);
  } catch (e) {
    // Cache entries are capped at 100KB; oversized sheets just skip caching.
  }
  return rows;
}

/**
 * Append one row. `obj` keys should match SCHEMA[sheetName]; missing keys
 * are written as empty strings.
 */
function appendRow(sheetName, obj) {
  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  try {
    const sheet = sheet_(sheetName);
    const header = SCHEMA[sheetName];
    if (!header) throw new Error('No schema for sheet: ' + sheetName);
    const row = header.map(function (h) { return obj[h] === undefined ? '' : obj[h]; });
    sheet.appendRow(row);
    invalidate_(sheetName);
  } finally {
    lock.releaseLock();
  }
}

/**
 * Append multiple rows in a single setValues call. Much faster than
 * appendRow in a loop for CSV imports.
 */
function appendRows(sheetName, objs) {
  if (!objs.length) return;
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const sheet = sheet_(sheetName);
    const header = SCHEMA[sheetName];
    const rows = objs.map(function (obj) {
      return header.map(function (h) { return obj[h] === undefined ? '' : obj[h]; });
    });
    sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, header.length).setValues(rows);
    invalidate_(sheetName);
  } finally {
    lock.releaseLock();
  }
}

/**
 * Update or insert a row identified by one or two key columns.
 * keys: either a string "col" or an array ["col1","col2"].
 * keyValues: the value(s) to match.
 * updates: partial object; only these columns are written on update.
 */
function upsertRow(sheetName, keys, keyValues, updates) {
  const keyArr = Array.isArray(keys) ? keys : [keys];
  const valArr = Array.isArray(keyValues) ? keyValues : [keyValues];

  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  try {
    const sheet = sheet_(sheetName);
    const header = SCHEMA[sheetName];
    const lastRow = sheet.getLastRow();
    if (lastRow >= 2) {
      const values = sheet.getRange(2, 1, lastRow - 1, header.length).getValues();
      const keyIdx = keyArr.map(function (k) { return header.indexOf(k); });
      for (let i = 0; i < values.length; i++) {
        let match = true;
        for (let k = 0; k < keyIdx.length; k++) {
          if (String(values[i][keyIdx[k]]) !== String(valArr[k])) { match = false; break; }
        }
        if (match) {
          // Update in place.
          const rowNum = i + 2;
          const newRow = values[i].slice();
          for (const col in updates) {
            const idx = header.indexOf(col);
            if (idx >= 0) newRow[idx] = updates[col];
          }
          sheet.getRange(rowNum, 1, 1, header.length).setValues([newRow]);
          invalidate_(sheetName);
          return { inserted: false, row: rowNum };
        }
      }
    }
    // Not found → insert.
    const newObj = Object.assign({}, updates);
    for (let k = 0; k < keyArr.length; k++) newObj[keyArr[k]] = valArr[k];
    const row = header.map(function (h) { return newObj[h] === undefined ? '' : newObj[h]; });
    sheet.appendRow(row);
    invalidate_(sheetName);
    return { inserted: true, row: sheet.getLastRow() };
  } finally {
    lock.releaseLock();
  }
}

/**
 * Find a single row by equality on one column. Returns the object or null.
 */
function findOne(sheetName, column, value) {
  const rows = readAll(sheetName);
  const target = String(value);
  for (let i = 0; i < rows.length; i++) {
    if (String(rows[i][column]) === target) return rows[i];
  }
  return null;
}

/**
 * Filter rows by a predicate function.
 */
function findWhere(sheetName, predicate) {
  return readAll(sheetName).filter(predicate);
}

/**
 * Delete the first row matching keyColumn = keyValue. Returns true if a row
 * was removed.
 */
function deleteRowByKey(sheetName, keyColumn, keyValue) {
  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  try {
    const sheet = sheet_(sheetName);
    const header = SCHEMA[sheetName];
    const keyIdx = header.indexOf(keyColumn);
    if (keyIdx < 0) throw new Error('Unknown column: ' + keyColumn);
    const lastRow = sheet.getLastRow();
    if (lastRow < 2) return false;
    const values = sheet.getRange(2, 1, lastRow - 1, header.length).getValues();
    const target = String(keyValue);
    for (let i = 0; i < values.length; i++) {
      if (String(values[i][keyIdx]) === target) {
        sheet.deleteRow(i + 2);
        invalidate_(sheetName);
        return true;
      }
    }
    return false;
  } finally {
    lock.releaseLock();
  }
}

/**
 * Delete every row where keyColumn = keyValue. Returns the count deleted.
 * Used for cascades (e.g. drop StudyProgress rows when a card is deleted).
 */
function deleteRowsByKey(sheetName, keyColumn, keyValue) {
  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  try {
    const sheet = sheet_(sheetName);
    const header = SCHEMA[sheetName];
    const keyIdx = header.indexOf(keyColumn);
    if (keyIdx < 0) throw new Error('Unknown column: ' + keyColumn);
    const lastRow = sheet.getLastRow();
    if (lastRow < 2) return 0;
    const values = sheet.getRange(2, 1, lastRow - 1, header.length).getValues();
    const target = String(keyValue);
    let removed = 0;
    for (let i = values.length - 1; i >= 0; i--) {
      if (String(values[i][keyIdx]) === target) {
        sheet.deleteRow(i + 2);
        removed += 1;
      }
    }
    if (removed) invalidate_(sheetName);
    return removed;
  } finally {
    lock.releaseLock();
  }
}

/**
 * Generate a short unique id with an optional prefix.
 */
function genId(prefix) {
  const ts = Date.now().toString(36);
  const rand = Math.random().toString(36).slice(2, 8);
  return (prefix || 'id') + '_' + ts + rand;
}

/**
 * Ensures every sheet from SHEETS exists with the right header row.
 * Safe to re-run — does not touch existing data.
 *
 * Handles the v1→v2 schema migration that inserted a `section` column
 * into Flashcards and Questions: if an existing sheet's pre-section
 * header is detected, a blank column is inserted before the header is
 * rewritten so existing rows stay aligned.
 */
function ensureSheets() {
  const ss = db_();
  for (const key in SHEETS) {
    const name = SHEETS[key];
    let sheet = ss.getSheetByName(name);
    if (!sheet) sheet = ss.insertSheet(name);
    const header = SCHEMA[name];
    migratePreSectionSchema_(sheet, name);
    const existing = sheet.getRange(1, 1, 1, Math.max(header.length, sheet.getLastColumn() || 1)).getValues()[0];
    const needsHeader = header.some(function (h, i) { return existing[i] !== h; });
    if (needsHeader) {
      sheet.getRange(1, 1, 1, header.length).setValues([header]);
      sheet.setFrozenRows(1);
    }
    invalidate_(name);
  }
}

/**
 * If `sheet` has the old header shape that lacked a `section` column at
 * index 2, insert a blank column there so existing rows align with the
 * new schema. No-op if the schema is already current or the sheet is
 * empty.
 */
function migratePreSectionSchema_(sheet, name) {
  if (name !== SHEETS.FLASHCARDS && name !== SHEETS.QUESTIONS) return;
  if (sheet.getLastColumn() < 3) return;
  const existing = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  // Old Flashcards: cardId, subject, front, ...
  // Old Questions: questionId, subject, prompt, ...
  const oldThirdCol = name === SHEETS.FLASHCARDS ? 'front' : 'prompt';
  if (existing[2] === oldThirdCol && existing[1] === 'subject') {
    sheet.insertColumnBefore(3);
    sheet.getRange(1, 3).setValue('section');
  }
}
