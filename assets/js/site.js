/* Divine AfterCare — interaction layer. Small, dependency-free. */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- header condenses on scroll ---- */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- mobile drawer ---- */
  var burger = document.querySelector('.burger');
  var drawer = document.getElementById('drawer');
  if (burger && drawer) {
    var setMenu = function (open) {
      document.body.classList.toggle('menu-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      drawer.setAttribute('aria-hidden', String(!open));
    };
    burger.addEventListener('click', function () {
      setMenu(!document.body.classList.contains('menu-open'));
    });
    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('menu-open')) setMenu(false);
    });
    setMenu(false);
  }

  /* ---- scroll reveal ---- */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var delay = el.dataset.delay ? parseInt(el.dataset.delay, 10) : 0;
          setTimeout(function () { el.classList.add('is-in'); }, delay);
          io.unobserve(el);
        });
      }, { rootMargin: '0px 0px -12% 0px', threshold: 0.06 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- hour dials: draw the arc for hours covered out of 24 ---- */
  var dials = document.querySelectorAll('.dial[data-hours]');
  if (dials.length) {
    var draw = function (dial) {
      var hours = parseFloat(dial.dataset.hours) || 0;
      var circle = dial.querySelector('.dial-fill');
      if (!circle) return;
      var r = circle.r.baseVal.value;
      var circumference = 2 * Math.PI * r;
      dial.style.setProperty('--dash', (circumference * Math.min(hours / 24, 1)).toFixed(2));
    };
    if (reduce || !('IntersectionObserver' in window)) {
      dials.forEach(draw);
    } else {
      var dio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          draw(entry.target);
          dio.unobserve(entry.target);
        });
      }, { threshold: 0.4 });
      dials.forEach(function (d) { dio.observe(d); });
    }
  }

  /* ---- sticky sub-nav active state ---- */
  var subnavLinks = document.querySelectorAll('.subnav a[href^="#"]');
  if (subnavLinks.length && 'IntersectionObserver' in window) {
    var targets = [];
    subnavLinks.forEach(function (a) {
      var t = document.querySelector(a.getAttribute('href'));
      if (t) targets.push(t);
    });
    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        subnavLinks.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    targets.forEach(function (t) { sio.observe(t); });
  }

  /* ---- inquiry form ----
     No backend on this build: the form validates, then hands off to the
     visitor's mail client with everything pre-filled. Swap `handoff` for a
     fetch() to your endpoint when the backend lands. */
  var form = document.getElementById('inquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var get = function (k) { return (data.get(k) || '').toString().trim(); };
      var lines = [
        'Name: ' + get('name'),
        'Phone: ' + get('phone'),
        'Email: ' + get('email'),
        'Procedure / care needed: ' + get('procedure'),
        'Surgery or start date: ' + (get('date') || 'Not yet scheduled'),
        'Care location: ' + get('location'),
        'Coverage needed: ' + get('duration'),
        '',
        get('message') || '(no additional details)'
      ];
      var status = form.querySelector('.form-status');
      if (status) {
        status.textContent = 'Opening your email app with this inquiry ready to send. If nothing opens, call (949) 787-6445 or write to info@divineaftercare.com.';
        status.classList.add('is-ok');
      }
      window.location.href =
        'mailto:info@divineaftercare.com'
        + '?subject=' + encodeURIComponent('Private inquiry — ' + (get('name') || 'Divine AfterCare'))
        + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }

  /* ---- year stamp ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
