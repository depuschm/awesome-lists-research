(function () {
  const NS = 'http://www.w3.org/2000/svg';
  const tip = document.getElementById('tip');

  function S(tag, attrs, parent) {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function T(parent, x, y, s, cls, anchor) {
    const t = S('text', { x, y, class: cls || 't-axis', 'text-anchor': anchor || 'start' }, parent);
    t.textContent = s;
    return t;
  }
  function H(tag, cls, html) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function k(n) {
    if (n >= 1e6) return (n / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
    if (n >= 1e4) return Math.round(n / 1e3) + 'k';
    if (n >= 1e3) return (n / 1e3).toFixed(1).replace(/\.0$/, '') + 'k';
    return String(n);
  }
  const fmt = n => n.toLocaleString('en-US');
  function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

  function placeTip(ev) {
    const pad = 14;
    const r = tip.getBoundingClientRect();
    let x = ev.clientX + pad, y = ev.clientY + pad;
    if (x + r.width > window.innerWidth - 8) x = ev.clientX - r.width - pad;
    if (y + r.height > window.innerHeight - 8) y = ev.clientY - r.height - pad;
    tip.style.left = Math.max(8, x) + 'px';
    tip.style.top = Math.max(8, y) + 'px';
  }
  function showTip(html, ev) { tip.innerHTML = html; tip.hidden = false; placeTip(ev); }
  function hideTip() { tip.hidden = true; }
  function bindTip(el, fn) {
    el.addEventListener('pointerenter', e => showTip(fn(), e));
    el.addEventListener('pointermove', placeTip);
    el.addEventListener('pointerleave', hideTip);
  }
  // column with 4px rounded data-end, square at the baseline
  function colPath(x, y, w, h, r) {
    r = Math.max(0, Math.min(r, w / 2, h));
    return `M${x},${y + h}V${y + r}Q${x},${y} ${x + r},${y}H${x + w - r}Q${x + w},${y} ${x + w},${y + r}V${y + h}Z`;
  }

  /* ---------- 1. GitHub top 100 unit chart ---------- */
  function top100(body) {
    const groups = [['list', 'Curated link lists'], ['guide', 'Guides, books and courses'], ['coll', 'AI skills, configs and other collections'], ['soft', 'Software']];
    const counts = {};
    DATA.top100.forEach(d => { counts[d[3]] = (counts[d[3]] || 0) + 1; });
    const lg = H('div', 'legend');
    groups.forEach(([g, label]) => lg.appendChild(H('span', 'key', `<i class="sw u-${g}"></i>${label} <b>${counts[g] || 0}</b>`)));
    body.appendChild(lg);
    const wrap = H('div', 'unit-wrap');
    body.appendChild(wrap);
    const W = body.clientWidth;
    const side = W >= 760;
    const cols = 10, gap = 4, labelW = 52;
    const cell = Math.max(14, Math.min(38, Math.floor((W - labelW - gap * (cols - 1)) / cols)));
    const width = labelW + cols * cell + (cols - 1) * gap, height = 10 * cell + 9 * gap;
    const svg = S('svg', { width, height }, wrap);
    const names = Object.fromEntries(groups);
    if (side) {
      const top10 = DATA.top100.slice(0, 10).filter(d => d[3] === 'list');
      const aside = H('div', 'unit-aside');
      aside.appendChild(H('div', 'ua-h', 'Curated lists in the top 10'));
      const ol = H('ul', 'ua-list');
      top10.forEach(d => ol.appendChild(H('li', '', `<span class="ua-r">#${d[0]}</span> ${esc(d[1])} <span class="ua-s">${k(d[2])}</span>`)));
      aside.appendChild(ol);
      aside.appendChild(H('p', 'ua-note', 'Nine of the top 25 and fifteen of the top 100 are curated lists. Almost half of the top 100 are not software at all.'));
      wrap.appendChild(aside);
    }
    for (let r = 0; r < 10; r++) T(svg, labelW - 10, r * (cell + gap) + cell / 2 + 4, `${r * 10 + 1}–${r * 10 + 10}`, 't-muted', 'end');
    DATA.top100.forEach((d, i) => {
      const r = Math.floor(i / cols), c = i % cols;
      const rect = S('rect', { x: labelW + c * (cell + gap), y: r * (cell + gap), width: cell, height: cell, rx: 3, class: `unit u-${d[3]}` }, svg);
      bindTip(rect, () => `<b>#${d[0]} ${esc(d[1])}</b><br>${fmt(d[2])} stars<br><span class="mut">${names[d[3]]}</span>`);
    });
  }

  /* ---------- 2. cohorts ---------- */
  function columns(body, rows, opt) {
    const W = body.clientWidth, Hh = opt.height || 250;
    const m = { t: 22, r: 6, b: 30, l: 44 };
    const iw = W - m.l - m.r, ih = Hh - m.t - m.b;
    const svg = S('svg', { width: W, height: Hh }, body);
    const band = iw / rows.length, bw = Math.min(24, band * 0.62);
    const y = v => m.t + ih - (v / opt.max) * ih;
    opt.ticks.forEach(v => {
      S('line', { x1: m.l, x2: W - m.r, y1: y(v), y2: y(v), class: v === 0 ? 'axis-line' : 'grid-line' }, svg);
      T(svg, m.l - 8, y(v) + 4, opt.tickFmt(v), 't-axis', 'end');
    });
    rows.forEach((d, i) => {
      const cx = m.l + band * i + band / 2;
      const v = opt.value(d), yy = y(v);
      S('path', { d: colPath(cx - bw / 2, yy, bw, m.t + ih - yy, 4), class: opt.hi(d) ? 'bar-hi' : 'bar-lo' }, svg);
      const lab = opt.label(d, band);
      if (lab) T(svg, cx, yy - 7, lab, 't-ink', 'middle');
      const lbl = opt.xLabel(d, band);
      if (lbl) T(svg, cx, Hh - 8, lbl, 't-axis', 'middle');
      const hit = S('rect', { x: m.l + band * i, y: m.t, width: band, height: ih, class: 'bar-hit' }, svg);
      bindTip(hit, () => opt.tip(d));
    });
  }
  function cohorts(body) {
    const rows = DATA.cohorts.map(d => ({ year: d[0], n: d[1], n10: d[2], med: d[3], share: d[2] / d[1] }));
    const hiYears = new Set([2014, 2015, 2025, 2026]);
    columns(body, rows, {
      height: 260, max: 0.45, ticks: [0, 0.1, 0.2, 0.3, 0.4],
      tickFmt: v => Math.round(v * 100) + '%',
      value: d => d.share,
      hi: d => hiYears.has(d.year),
      label: (d, band) => hiYears.has(d.year) && !(band < 34 && d.year === 2025) ? Math.round(d.share * 100) + '%' : '',
      xLabel: (d, band) => band >= 38 ? String(d.year) : (band >= 22 ? '’' + String(d.year).slice(2) : (d.year % 4 === 2 ? '’' + String(d.year).slice(2) : '')),
      tip: d => `<b>Started in ${d.year}</b><br>${d.n10} of ${d.n} lists reached 10k+ stars (${Math.round(d.share * 100)}%)<br><span class="mut">Median ${fmt(d.med)} stars</span>`,
    });
  }

  /* ---------- 3. dumbbell ---------- */
  function dumbbell(body) {
    const lg = H('div', 'legend');
    lg.appendChild(H('span', 'key', '<i class="dot dot-lo-legend"></i>Lists under 2k stars'));
    lg.appendChild(H('span', 'key', '<i class="dot dot-hi-legend"></i>Lists with 50k+ stars'));
    body.appendChild(lg);
    const W = body.clientWidth, narrow = W < 620;
    const labelW = narrow ? 0 : 236, right = 74;
    const x0 = labelW + (narrow ? 8 : 16), x1 = W - right;
    const x = v => x0 + (v / 100) * (x1 - x0);
    const rowH = narrow ? 50 : 32, headH = 36;
    const groups = [['same', 'About the same at every tier'], ['more', 'More common among the most-starred']];
    let total = 26;
    groups.forEach(([g]) => { total += headH + DATA.dumbbell.filter(d => d[0] === g).length * rowH; });
    const svg = S('svg', { width: W, height: total }, body);
    [0, 25, 50, 75, 100].forEach(v => {
      S('line', { x1: x(v), x2: x(v), y1: 18, y2: total, class: v === 0 ? 'axis-line' : 'grid-line' }, svg);
      T(svg, x(v), 12, v + '%', 't-axis', 'middle');
    });
    let yCur = 26;
    groups.forEach(([g, title]) => {
      T(svg, 0, yCur + 24, title, 't-head');
      yCur += headH;
      DATA.dumbbell.filter(d => d[0] === g).forEach(d => {
        const [, label, hi, lo, rho] = d;
        const cy = yCur + (narrow ? 32 : rowH / 2);
        if (narrow) T(svg, 0, yCur + 14, label, 't-label');
        else T(svg, 0, cy + 4.5, label, 't-label');
        S('line', { x1: x(Math.min(hi, lo)), x2: x(Math.max(hi, lo)), y1: cy, y2: cy, class: 'db-line' }, svg);
        S('circle', { cx: x(lo), cy, r: 5.5, class: 'dot-lo' }, svg);
        S('circle', { cx: x(hi), cy, r: 5.5, class: 'dot-hi' }, svg);
        const right = Math.max(hi, lo), left = Math.min(hi, lo);
        T(svg, x(right) + 10, cy + 4.5, Math.round(right) + '%', 't-ink');
        T(svg, x(left) - 10, cy + 4.5, Math.round(left) + '%', 't-ink', 'end');
        const hit = S('rect', { x: 0, y: yCur, width: W, height: rowH, class: 'bar-hit' }, svg);
        bindTip(hit, () => `<b>${esc(label)}</b><br>50k+ stars: ${hi.toFixed(0)}%<br>Under 2k stars: ${lo.toFixed(0)}%<br><span class="mut">Spearman ρ with stars: ${rho >= 0 ? '+' : ''}${rho.toFixed(2)}</span>`);
        yCur += rowH;
      });
    });
  }

  /* ---------- 4. scatter ---------- */
  function scatter(body) {
    const W = body.clientWidth, Hh = W < 600 ? 330 : 430;
    const m = { t: 14, r: 18, b: 44, l: 54 };
    const iw = W - m.l - m.r, ih = Hh - m.t - m.b;
    const lx = Math.log10, X0 = lx(10), X1 = lx(20000), Y0 = lx(900), Y1 = lx(700000);
    const x = v => m.l + (lx(Math.max(10, v)) - X0) / (X1 - X0) * iw;
    const y = v => m.t + ih - (lx(v) - Y0) / (Y1 - Y0) * ih;
    const svg = S('svg', { width: W, height: Hh }, body);
    [1000, 10000, 100000].forEach(v => { S('line', { x1: m.l, x2: W - m.r, y1: y(v), y2: y(v), class: 'grid-line' }, svg); T(svg, m.l - 8, y(v) + 4, k(v), 't-axis', 'end'); });
    [10, 100, 1000, 10000].forEach(v => { S('line', { x1: x(v), x2: x(v), y1: m.t, y2: m.t + ih, class: 'grid-line' }, svg); T(svg, x(v), m.t + ih + 18, k(v), 't-axis', 'middle'); });
    S('line', { x1: m.l, x2: W - m.r, y1: m.t + ih, y2: m.t + ih, class: 'axis-line' }, svg);
    T(svg, m.l + iw, Hh - 4, 'Entries in README →', 't-muted', 'end');
    T(svg, m.l - 46, m.t - 2, 'Stars', 't-muted');
    const pts = DATA.scatter.map(d => ({ repo: d[0], stars: d[1], n: d[2], year: d[3], px: x(d[2]), py: y(d[1]) }));
    const labels = { 'vinta/awesome-python': 'end', 'avelino/awesome-go': 'end', 'enaqx/awesome-react': 'end', 'hesreallyhim/awesome-claude-code': 'start', 'uhub/awesome-python': 'end', 'rust-unofficial/awesome-rust': 'start' };
    const g = S('g', {}, svg);
    pts.forEach(p => S('circle', { cx: p.px, cy: p.py, r: 4, class: labels[p.repo] ? 'sc-hi' : 'sc-dot' }, g));
    pts.filter(p => labels[p.repo]).forEach(p => {
      const a = labels[p.repo];
      if (W < 520 && (p.repo === 'rust-unofficial/awesome-rust' || p.repo === 'enaqx/awesome-react')) return;
      const aa = (W < 600 && p.repo === 'hesreallyhim/awesome-claude-code') ? 'end' : a;
      T(svg, p.px + (aa === 'end' ? -9 : 9), p.py + 4, p.repo, 't-ink halo', aa);
    });
    const ring = S('circle', { r: 7, class: 'sc-ring', visibility: 'hidden' }, svg);
    const overlay = S('rect', { x: m.l, y: m.t, width: iw, height: ih, class: 'bar-hit' }, svg);
    overlay.addEventListener('pointermove', ev => {
      const b = svg.getBoundingClientRect(), mx = ev.clientX - b.left, my = ev.clientY - b.top;
      let best = null, bd = 196;
      pts.forEach(p => { const dd = (p.px - mx) ** 2 + (p.py - my) ** 2; if (dd < bd) { bd = dd; best = p; } });
      if (!best) { ring.setAttribute('visibility', 'hidden'); hideTip(); return; }
      ring.setAttribute('cx', best.px); ring.setAttribute('cy', best.py); ring.setAttribute('visibility', 'visible');
      showTip(`<b>${esc(best.repo)}</b><br>${fmt(best.stars)} stars · ${fmt(best.n)} entries<br><span class="mut">First commit ${best.year}</span>`, ev);
    });
    overlay.addEventListener('pointerleave', () => { ring.setAttribute('visibility', 'hidden'); hideTip(); });
  }

  /* ---------- 5. growth small multiples ---------- */
  function niceMax(v) {
    const p = Math.pow(10, Math.floor(Math.log10(v)));
    for (const s of [1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]) if (s * p >= v) return s * p;
    return 10 * p;
  }
  function growth(body) {
    const grid = H('div', 'panels');
    body.appendChild(grid);
    const t0 = Date.UTC(2014, 6, 1), t1 = Date.UTC(2026, 9, 25);
    const toT = s => { const [a, b, c] = s.split('-').map(Number); return Date.UTC(a, b - 1, c); };
    const panels = DATA.growth.map(([repo, note, pts]) => {
      const p = H('div', 'panel');
      p.appendChild(H('div', 'pt', esc(repo)));
      p.appendChild(H('div', 'pn', esc(note)));
      const holder = H('div', '');
      p.appendChild(holder);
      grid.appendChild(p);
      return { repo, pts, holder };
    });
    panels.forEach(({ pts, holder }) => {
      const W = holder.clientWidth || 220, Hh = 128;
      const m = { t: 18, r: 34, b: 20, l: 4 };
      const iw = W - m.l - m.r, ih = Hh - m.t - m.b;
      const data = pts.map(([d, e]) => ({ t: toT(d), d, e }));
      const peak = data.reduce((a, b) => (b.e > a.e ? b : a));
      const ymax = niceMax(peak.e * 1.08);
      const x = t => m.l + (t - t0) / (t1 - t0) * iw;
      const y = v => m.t + ih - v / ymax * ih;
      const svg = S('svg', { width: W, height: Hh }, holder);
      S('line', { x1: m.l, x2: m.l + iw, y1: y(ymax), y2: y(ymax), class: 'grid-line' }, svg);
      T(svg, m.l + iw + 4, y(ymax) + 4, k(ymax), 't-muted');
      S('line', { x1: m.l, x2: m.l + iw, y1: y(0), y2: y(0), class: 'axis-line' }, svg);
      T(svg, m.l + iw + 4, y(0) + 4, '0', 't-muted');
      [2014, 2018, 2022, 2026].forEach(yr => { const xx = x(Date.UTC(yr, 0, 1)); if (xx >= m.l) T(svg, xx, Hh - 4, '’' + String(yr).slice(2), 't-muted', 'middle'); });
      const line = data.map((p, i) => `${i ? 'L' : 'M'}${x(p.t).toFixed(1)},${y(p.e).toFixed(1)}`).join('');
      S('path', { d: line + `L${x(data[data.length - 1].t)},${y(0)}L${x(data[0].t)},${y(0)}Z`, class: 'ar' }, svg);
      S('path', { d: line, class: 'ln' }, svg);
      const last = data[data.length - 1];
      S('circle', { cx: x(last.t), cy: y(last.e), r: 4, class: 'mk' }, svg);
      if (peak !== last && (peak.e - last.e) / peak.e > 0.05) {
        S('circle', { cx: x(peak.t), cy: y(peak.e), r: 4, class: 'mk' }, svg);
        const left = x(peak.t) > m.l + iw * 0.6;
        T(svg, x(peak.t) + (left ? -7 : 7), y(peak.e) - 6, 'peak ' + fmt(peak.e), 't-ink', left ? 'end' : 'start');
        T(svg, x(last.t) - 4, y(last.e) + 18 > m.t + ih ? y(last.e) - 9 : y(last.e) + 18, 'now ' + fmt(last.e), 't-ink', 'end');
      } else {
        T(svg, x(last.t) - 8, y(last.e) - 8, fmt(last.e), 't-ink', 'end');
      }
      const xh = S('line', { y1: m.t, y2: m.t + ih, class: 'xhair', visibility: 'hidden' }, svg);
      const dot = S('circle', { r: 4.5, class: 'mk', visibility: 'hidden' }, svg);
      const overlay = S('rect', { x: m.l, y: 0, width: iw, height: Hh, class: 'bar-hit' }, svg);
      overlay.addEventListener('pointermove', ev => {
        const b = svg.getBoundingClientRect(), mx = ev.clientX - b.left;
        let best = data[0];
        data.forEach(p => { if (Math.abs(x(p.t) - mx) < Math.abs(x(best.t) - mx)) best = p; });
        xh.setAttribute('x1', x(best.t)); xh.setAttribute('x2', x(best.t)); xh.setAttribute('visibility', 'visible');
        dot.setAttribute('cx', x(best.t)); dot.setAttribute('cy', y(best.e)); dot.setAttribute('visibility', 'visible');
        const label = best === last ? 'Now (Oct 2026)' : new Date(best.t - 864e5).toLocaleDateString('en-US', { month: 'short', year: 'numeric', timeZone: 'UTC' });
        showTip(`<b>${label}</b><br>${fmt(best.e)} entries`, ev);
      });
      overlay.addEventListener('pointerleave', () => { xh.setAttribute('visibility', 'hidden'); dot.setAttribute('visibility', 'hidden'); hideTip(); });
    });
  }

  /* ---------- 6. dormant star growth ---------- */
  function dormant(body) {
    const rows = DATA.dormant.map(d => ({ b: d[0], n: d[1], r: d[2], g: d[2] - 1 }));
    columns(body, rows, {
      height: 240, max: 0.36, ticks: [0, 0.1, 0.2, 0.3],
      tickFmt: v => '+' + Math.round(v * 100) + '%',
      value: d => Math.max(0, d.g),
      hi: () => true,
      label: d => '+' + Math.round(d.g * 100) + '%',
      xLabel: d => d.b,
      tip: d => `<b>Last content update ${d.b} ago</b><br>${d.n} lists<br><span class="mut">Median stars now ÷ stars then: ×${d.r.toFixed(2)}</span>`,
    });
  }

  const R = { top100, cohorts, dumbbell, scatter, growth, dormant };
  function render(fig) {
    const body = fig.querySelector('.chart-body');
    body.innerHTML = '';
    try { R[fig.dataset.chart](body); } catch (e) { body.textContent = 'Chart failed to render.'; console.error(e); }
  }
  const figs = Array.from(document.querySelectorAll('figure.chart'));
  figs.forEach(render);
  let lastW = figs.map(f => f.clientWidth);
  let timer = null;
  window.addEventListener('resize', () => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      figs.forEach((f, i) => { if (f.clientWidth !== lastW[i]) { lastW[i] = f.clientWidth; render(f); } });
    }, 120);
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => figs.forEach(render));
})();
