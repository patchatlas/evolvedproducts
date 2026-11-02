// Fleet calculator: 1 oz concentrate per 55 gallons; 32 oz per bottle.
(function () {
  var gal = document.getElementById('gal');
  if (gal) {
    var upd = function () {
      var g = Math.max(0, parseFloat(gal.value) || 0);
      var oz = g / 55;
      document.getElementById('drums').textContent = Math.ceil(g / 55).toLocaleString();
      document.getElementById('oz').textContent = (Math.round(oz * 10) / 10).toLocaleString();
      document.getElementById('bottles').textContent = Math.ceil(oz / 32).toLocaleString();
    };
    gal.addEventListener('input', upd); upd();
  }

  // Contact form: prefill from ?topic=&product=, then open the visitor's email app.
  var form = document.getElementById('contact-form');
  if (form) {
    var q = new URLSearchParams(location.search);
    if (q.get('topic')) form.topic.value = q.get('topic');
    if (q.get('product')) form.product.value = q.get('product');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var t = form.topic.options[form.topic.selectedIndex].text;
      var lines = [
        'Request: ' + t,
        'Product: ' + (form.product.value || 'Not sure yet'),
        'Quantity: ' + form.qty.value,
        'Name: ' + form.name.value,
        'Company: ' + form.company.value,
        '', form.msg.value
      ];
      location.href = 'mailto:Tyler@evolvedproducts.us?subject=' +
        encodeURIComponent('EVOLVED website: ' + t) + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }
})();
