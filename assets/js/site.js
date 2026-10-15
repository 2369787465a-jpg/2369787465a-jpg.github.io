/* Progressive enhancement: navigation and all page content work without JS. */
(() => {
  const button = document.querySelector('.menu-toggle');
  const navigation = document.getElementById('site-navigation');
  if (!button || !navigation || !window.matchMedia) return;
  const mobile = window.matchMedia('(max-width: 760px)');
  const setOpen = (open) => {
    button.setAttribute('aria-expanded', String(open));
    navigation.hidden = mobile.matches && !open;
  };
  const sync = () => {
    button.hidden = !mobile.matches;
    setOpen(false);
  };
  button.addEventListener('click', () => setOpen(button.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (mobile.matches && event.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mobile.matches && button.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      button.focus();
    }
  });
  if (mobile.addEventListener) mobile.addEventListener('change', sync);
  else mobile.addListener(sync);
  sync();
})();
