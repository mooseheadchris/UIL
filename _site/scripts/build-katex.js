#!/usr/bin/env node
/**
 * Bundle KaTeX into src/html/katex.html as a single HTML partial containing
 * inline CSS (with all woff2 fonts embedded as base64 data URIs) and inline
 * JS (katex.min.js + auto-render.min.js). This makes the web app fully
 * self-contained — no CDN requests at runtime.
 *
 * Usage, from any machine with npm + node:
 *   cd /tmp && npm pack katex@0.16.11
 *   tar -xzf katex-0.16.11.tgz
 *   node /path/to/acdec-site/scripts/build-katex.js
 *
 * Reads from ./package/dist (relative to CWD).
 * Writes to <repo>/src/html/katex.html.
 */
const fs = require('fs');
const path = require('path');

const DIST = path.resolve(process.cwd(), 'package', 'dist');
if (!fs.existsSync(DIST)) {
  console.error('Run from a directory containing ./package/dist from npm pack katex.');
  process.exit(1);
}

const repoRoot = path.resolve(__dirname, '..');
const target = path.join(repoRoot, 'src', 'html', 'katex.html');

const css = fs.readFileSync(path.join(DIST, 'katex.min.css'), 'utf8');
const js = fs.readFileSync(path.join(DIST, 'katex.min.js'), 'utf8');
const autoJs = fs.readFileSync(path.join(DIST, 'contrib', 'auto-render.min.js'), 'utf8');

// Replace each @font-face src list with a single woff2 data-URI entry.
// KaTeX emits:  src:url(fonts/X.woff2) format("woff2"),url(X.woff) ...,url(X.ttf) ...;
const rewritten = css.replace(
  /src:url\(fonts\/([^)]+)\.woff2\)[^;]*;/g,
  function (_, name) {
    const b64 = fs.readFileSync(path.join(DIST, 'fonts', name + '.woff2')).toString('base64');
    return 'src:url(data:font/woff2;base64,' + b64 + ') format("woff2");';
  }
);

const stillUnresolved = rewritten.match(/url\(fonts\//g);
if (stillUnresolved) {
  console.error('ERROR: ' + stillUnresolved.length + ' font URLs could not be inlined.');
  process.exit(2);
}

const out = [
  '<style>', rewritten, '</style>',
  '<script>', js, '</script>',
  '<script>', autoJs, '</script>',
  ''
].join('\n');

fs.writeFileSync(target, out);
console.log('Wrote ' + target + '  (' + Math.round(out.length / 1024) + ' KB)');
