(function () {
  'use strict';

  var header = document.querySelector('[data-header]');
  var toggle = document.querySelector('[data-nav-toggle]');
  var nav = document.querySelector('[data-nav]');
  var year = document.querySelector('[data-year]');

  if (year) year.textContent = String(new Date().getFullYear());

  if (header) {
    var updateHeader = function () { header.classList.toggle('is-scrolled', window.scrollY > 12); };
    updateHeader();
    window.addEventListener('scroll', updateHeader, { passive: true });
  }

  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      var label = toggle.querySelector('.sr-only');
      if (label) label.textContent = open ? 'Close navigation' : 'Open navigation';
      nav.classList.toggle('is-open', open);
      if (header) header.classList.toggle('nav-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    };
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    nav.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', function () { setOpen(false); }); });
    document.addEventListener('keydown', function (event) { if (event.key === 'Escape') setOpen(false); });
  }

  /* Contact form: async submit to Web3Forms, no page reload. Same wiring as the previous production site. */
  var form = document.getElementById('projectForm');
  var status = document.getElementById('formStatus');
  if (form && status) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      var idleLabel = btn.textContent;

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      btn.disabled = true;
      btn.textContent = 'Sending...';
      status.className = 'form-status';
      status.textContent = '';

      fetch(form.action, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      })
        .then(function (res) { return res.json().catch(function () { return { success: res.ok }; }); })
        .then(function (data) {
          if (data.success) {
            form.reset();
            status.className = 'form-status ok';
            status.textContent = 'Thank you. We have your enquiry and will respond within one business day.';
          } else {
            throw new Error('Submission failed');
          }
        })
        .catch(function () {
          status.className = 'form-status err';
          status.innerHTML = 'Something went wrong. Please email <a href="mailto:projects@alphaitengineering.com">projects@alphaitengineering.com</a> directly.';
        })
        .finally(function () {
          btn.disabled = false;
          btn.textContent = idleLabel;
        });
    });
  }
})();
