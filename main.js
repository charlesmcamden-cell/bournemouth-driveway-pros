// Bournemouth Driveway Pros — site interactions
document.addEventListener('DOMContentLoaded', function () {

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var mobilePanel = document.querySelector('.mobile-nav-panel');
  if (toggle && mobilePanel) {
    toggle.addEventListener('click', function () {
      var isOpen = mobilePanel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // FAQ accordion
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', function () {
      var wasOpen = item.classList.contains('open');
      item.closest('.faq-list').querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
      });
      if (!wasOpen) item.classList.add('open');
    });
  });

  // Quote form — real AJAX submission to the form's `action` (Formspree by default).
  // See README.md to activate: create a free Formspree form and swap FORM_ACTION
  // in generate_site.py for your real endpoint, then rebuild.
  document.querySelectorAll('form.quote-form').forEach(function (form) {
    var btn = form.querySelector('button[type="submit"]');
    var status = form.querySelector('.form-status');
    var placeholderAction = /YOUR_FORM_ID/.test(form.action);

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      if (placeholderAction) {
        // Endpoint not configured yet — tell the site owner, don't fake success to the visitor.
        status.style.display = 'block';
        status.style.color = '#e2551f';
        status.textContent = 'Form isn\'t connected yet — see README.md to activate lead capture.';
        return;
      }

      var original = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending...';
      status.style.display = 'none';

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            status.style.color = '#0f9d8f';
            status.textContent = 'Thanks! We\'ll be in touch shortly.';
          } else {
            status.style.color = '#e2551f';
            status.textContent = 'Something went wrong — please call us instead.';
          }
          status.style.display = 'block';
        })
        .catch(function () {
          status.style.color = '#e2551f';
          status.textContent = 'Something went wrong — please call us instead.';
          status.style.display = 'block';
        })
        .finally(function () {
          btn.disabled = false;
          btn.textContent = original;
        });
    });
  });

  // Reveal sticky mobile CTA after scrolling past hero
  var sticky = document.querySelector('.sticky-cta');
  if (sticky) {
    window.addEventListener('scroll', function () {
      sticky.style.transform = window.scrollY > 400 ? 'translateY(0)' : 'translateY(100%)';
    });
  }
});
