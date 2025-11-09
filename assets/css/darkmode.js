document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('dark-toggle');
  if (!toggle) return;
  toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    localStorage.setItem('darkmode', document.body.classList.contains('dark'));
  });
  if (localStorage.getItem('darkmode') === 'true') {
    document.body.classList.add('dark');
  }
});
