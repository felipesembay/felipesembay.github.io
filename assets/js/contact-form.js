/**
 * Contact Form Handler — Formspree (static-site compatible)
 *
 * HOW TO SET UP:
 *  1. Go to https://formspree.io and sign in with felipesembay91@gmail.com
 *  2. Click "New Form", give it a name (e.g. "Portfolio Contact")
 *  3. Copy the form endpoint, e.g. https://formspree.io/f/xabcdefg
 *  4. Replace FORMSPREE_ENDPOINT below with your real endpoint
 *
 * The form will then send emails directly to felipesembay91@gmail.com
 * Free plan: 50 submissions/month — more than enough for a portfolio.
 */

(function () {
  'use strict';

  // ─── CONFIG ────────────────────────────────────────────────────────────────
  // Replace with your Formspree endpoint after signing up at formspree.io
  const FORMSPREE_ENDPOINT = 'https://formspree.io/f/xwvngejk';
  // ───────────────────────────────────────────────────────────────────────────

  const forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const loading = form.querySelector('.loading');
      const errorMsg = form.querySelector('.error-message');
      const successMsg = form.querySelector('.sent-message');

      // Reset state
      loading.style.display = 'block';
      errorMsg.style.display = 'none';
      successMsg.style.display = 'none';

      const formData = new FormData(form);

      fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        body: formData,
        headers: {
          Accept: 'application/json',
        },
      })
        .then(function (response) {
          loading.style.display = 'none';
          if (response.ok) {
            successMsg.style.display = 'block';
            form.reset();
          } else {
            return response.json().then(function (data) {
              throw new Error(
                data.errors
                  ? data.errors.map((e) => e.message).join(', ')
                  : 'Oops! There was a problem. Please try again.'
              );
            });
          }
        })
        .catch(function (error) {
          loading.style.display = 'none';
          errorMsg.textContent = error.message || 'Oops! There was a problem. Please try again.';
          errorMsg.style.display = 'block';
        });
    });
  });
})();
