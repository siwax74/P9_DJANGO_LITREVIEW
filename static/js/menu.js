document.addEventListener('DOMContentLoaded', () => {
  const hamburgerButton = document.getElementById('hamburger-button');
  const navigationMenu = document.getElementById('navigation-menu');

  hamburgerButton.addEventListener('click', () => {
      // Toggle active class for button and menu
      hamburgerButton.classList.toggle('active');
      navigationMenu.classList.toggle('open');
  });
});