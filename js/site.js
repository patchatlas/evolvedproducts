(function () {
  // "+ Show More" toggles on home cards
  document.querySelectorAll('.more').forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.closest('.card'); c.classList.toggle('open');
      b.textContent = c.classList.contains('open') ? '− Show Less' : '+ Show More';
    });
  });

  // Gallery carousel with thumbnails
  var car = document.getElementById('carousel');
  if (car) {
    var track = car.querySelector('.track'), slides = track.children,
        thumbs = document.querySelectorAll('#thumbs img'), i = 0;
    var go = function (n) {
      i = (n + slides.length) % slides.length;
      var s = slides[i], off = s.offsetLeft - (car.clientWidth - s.clientWidth) / 2;
      track.style.transform = 'translateX(' + (-off) + 'px)';
      for (var k = 0; k < slides.length; k++) { slides[k].classList.toggle('on', k === i); thumbs[k] && thumbs[k].classList.toggle('on', k === i); }
    };
    car.querySelector('.prev').onclick = function () { go(i - 1); };
    car.querySelector('.next').onclick = function () { go(i + 1); };
    thumbs.forEach(function (t, k) { t.onclick = function () { go(k); }; });
    slides[0].loading = 'eager';
    window.addEventListener('resize', function () { go(i); });
    window.addEventListener('load', function () { go(0); }); go(0);
  }

  // Shop: category filter + show back of bottle on hover
  var cats = document.getElementById('cats');
  if (cats) {
    var filter = function (f, label) {
      cats.querySelectorAll('a').forEach(function (a) { a.classList.toggle('on', a.dataset.f === f); });
      document.getElementById('cat-title').textContent = label;
      document.querySelectorAll('.prod').forEach(function (p) {
        p.style.display = (f === 'all' || p.dataset.cat.indexOf(f) > -1) ? '' : 'none';
      });
    };
    cats.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { filter(a.dataset.f, a.textContent); });
    });
    var h = location.hash.slice(1);
    if (h === 'bugaway' || h === 'rainaway') filter(h, document.getElementById(h).textContent);
    document.querySelectorAll('.prod img').forEach(function (im) {
      var front = im.src, back = im.dataset.back;
      new Image().src = back;
      im.addEventListener('mouseenter', function () { im.src = back; });
      im.addEventListener('mouseleave', function () { im.src = front; });
    });
  }

  // Contact form: opens the visitor's email app with the message filled in
  var form = document.getElementById('contact-form');
  if (form) {
    var q = new URLSearchParams(location.search);
    if (q.get('product')) { form.product.value = q.get('product'); form.msg.value = 'I would like to order: ' + q.get('product') + '\nQuantity: \nShip to: '; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var body = 'Name: ' + form.name.value + '\nEmail: ' + form.email.value + '\n\n' + form.msg.value;
      location.href = 'mailto:Tyler@evolvedproducts.us?subject=' + encodeURIComponent(form.product.value ? 'Order: ' + form.product.value : 'Website message') + '&body=' + encodeURIComponent(body);
    });
  }
})();
