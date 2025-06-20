// ============================
// Mobile Menu Toggle Script
// ============================

// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Select the hamburger icon and nav menu
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.querySelector(".nav-menu");

  // Ensure both elements exist before attaching event
  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      menu.classList.toggle("show"); // Add or remove the 'show' class
    });
  }
});