/* FITNESS FACTORY — site script */
(function () {
  var html = document.documentElement;

  /* ---------- Language toggle ---------- */
  function applyTitle() {
    var t = html.getAttribute(html.lang === 'ar' ? 'data-title-ar' : 'data-title-en');
    if (t) document.title = t;
  }
  function setLang(l) {
    html.lang = l;
    html.dir = l === 'ar' ? 'rtl' : 'ltr';
    try { localStorage.setItem('ff-lang', l); } catch (e) {}
    applyTitle();
    renderHours();
  }
  document.querySelectorAll('[data-lang-toggle]').forEach(function (b) {
    b.addEventListener('click', function () { setLang(html.lang === 'ar' ? 'en' : 'ar'); });
  });
  applyTitle();

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.main-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------- Keep active branch tab visible ---------- */
  var activeTab = document.querySelector('.branch-nav a[aria-current="page"]');
  if (activeTab && activeTab.scrollIntoView) {
    try { activeTab.scrollIntoView({ block: 'nearest', inline: 'center' }); window.scrollTo(0, 0); } catch (e) {}
  }

  /* ---------- Opening hours / open-now (Amman time) ---------- */
  // hours: array indexed by JS day (0=Sun..6=Sat) of [openMinutes, closeMinutes]; close > 1440 = after midnight
  function ammanNow() {
    try {
      var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Amman', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      return { day: days[o.weekday], min: (parseInt(o.hour, 10) % 24) * 60 + parseInt(o.minute, 10) };
    } catch (e) {
      var d = new Date(); return { day: d.getDay(), min: d.getHours() * 60 + d.getMinutes() };
    }
  }
  function isOpen(hours, now) {
    var t = hours[now.day];
    if (t && now.min >= t[0] && now.min < t[1]) return true;
    var y = hours[(now.day + 6) % 7];
    if (y && y[1] > 1440 && now.min < y[1] - 1440) return true;
    return false;
  }
  function renderHours() {
    var now = ammanNow();
    var ar = html.lang === 'ar';
    document.querySelectorAll('[data-hours]').forEach(function (el) {
      var hours; try { hours = JSON.parse(el.getAttribute('data-hours')); } catch (e) { return; }
      var open = isOpen(hours, now);
      el.classList.toggle('open', open);
      el.classList.toggle('closed', !open);
      el.textContent = open ? (ar ? 'مفتوح الآن' : 'Open now') : (ar ? 'مغلق الآن' : 'Closed now');
    });
    document.querySelectorAll('[data-day]').forEach(function (el) {
      var isToday = parseInt(el.getAttribute('data-day'), 10) === now.day;
      el.classList.toggle(el.tagName === 'TR' ? 'today' : 'is-today', isToday);
      var pill = el.querySelector('.today-pill');
      if (pill) pill.hidden = !isToday;
    });
  }
  renderHours();

  /* ---------- WhatsApp floating menu ---------- */
  var waToggle = document.querySelector('[data-wa-toggle]');
  var waMenu = document.querySelector('.wa-menu');
  if (waToggle && waMenu) {
    waToggle.addEventListener('click', function (e) {
      e.preventDefault();
      var o = waMenu.classList.toggle('open');
      waToggle.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (!waMenu.contains(e.target) && !waToggle.contains(e.target)) waMenu.classList.remove('open');
    });
  }

  /* ---------- Gallery lightbox ---------- */
  var lb = document.querySelector('.lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    document.querySelectorAll('[data-full]').forEach(function (b) {
      b.addEventListener('click', function () {
        lbImg.src = b.getAttribute('data-full');
        lbImg.alt = b.querySelector('img') ? b.querySelector('img').alt : '';
        lb.classList.add('open');
      });
    });
    lb.addEventListener('click', function (e) { if (e.target !== lbImg) lb.classList.remove('open'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('open'); });
  }

  /* ---------- Reveal on scroll ---------- */
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- Year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
