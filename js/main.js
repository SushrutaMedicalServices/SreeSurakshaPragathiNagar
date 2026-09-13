document.addEventListener('DOMContentLoaded', function () {
  var here = window.location.pathname;
  document.querySelectorAll('.navbar__link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href === here || (href !== '/' && here.indexOf(href) === 0)) {
      link.classList.add('is-active');
    }
  });

  var primaryNav = document.getElementById('primaryNav');
  if (primaryNav && !primaryNav.querySelector('.navbar__link--cta')) {
    var cta = document.createElement('a');
    cta.href = '/book-an-appointment/';
    cta.className = 'navbar__link navbar__link--cta';
    cta.textContent = 'Book An Appointment';
    primaryNav.appendChild(cta);
  }

  var navbar = document.getElementById('navbar');
  var navToggle = document.getElementById('navToggle');
  if (navToggle && navbar) {
    navToggle.addEventListener('click', function () {
      navbar.classList.toggle('is-open');
      var expanded = navbar.classList.contains('is-open');
      navToggle.setAttribute('aria-expanded', expanded);
    });
  }

  var backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('is-visible', window.scrollY > 420);
    });
  }

  document.querySelectorAll('[data-lead-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var success = form.querySelector('.form-success');
      var data = new FormData(form);
      var subject = encodeURIComponent('Enquiry from ' + (data.get('name') || 'website visitor'));
      var bodyLines = [];
      data.forEach(function (value, key) { bodyLines.push(key + ': ' + value); });
      var body = encodeURIComponent(bodyLines.join('\n'));
      if (success) success.classList.add('is-visible');
      form.reset();
      window.setTimeout(function () {
        window.location.href = 'mailto:info@sushrutamedicalservices.com?subject=' + subject + '&body=' + body;
      }, 600);
    });
  });
});
