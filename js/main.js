(function () {
  'use strict';

  // --- Year in footer ---
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // --- Active nav highlighting (scroll spy) ---
  var links = Array.prototype.slice.call(document.querySelectorAll('.topbar-nav a'));
  var sections = links
    .map(function (a) {
      var id = a.getAttribute('href').slice(1);
      return document.getElementById(id);
    })
    .filter(Boolean);

  function highlight(id) {
    links.forEach(function (a) {
      var on = a.getAttribute('href') === '#' + id;
      a.classList.toggle('active', on);
      if (on) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) highlight(e.target.id);
        });
      },
      { rootMargin: '-35% 0px -60% 0px' }
    );
    sections.forEach(function (s) { io.observe(s); });
  } else {
    var onScroll = function () {
      var pos = window.scrollY + 100;
      var current = sections[0].id;
      sections.forEach(function (s) {
        if (s.offsetTop <= pos) current = s.id;
      });
      highlight(current);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // --- Printing: open all <details> course lists, then restore ---
  var details = Array.prototype.slice.call(document.querySelectorAll('details.courses'));
  var wasOpen = [];

  function expandForPrint() {
    wasOpen = details.map(function (d) { return d.open; });
    details.forEach(function (d) { d.open = true; });
  }
  function restoreAfterPrint() {
    details.forEach(function (d, i) { d.open = wasOpen[i] === true; });
  }

  window.addEventListener('beforeprint', expandForPrint);
  window.addEventListener('afterprint', restoreAfterPrint);
  // Safari / iOS don't fire beforeprint reliably:
  if (window.matchMedia) {
    var mql = window.matchMedia('print');
    if (mql.addEventListener) {
      mql.addEventListener('change', function (e) {
        if (e.matches) expandForPrint(); else restoreAfterPrint();
      });
    }
  }
})();