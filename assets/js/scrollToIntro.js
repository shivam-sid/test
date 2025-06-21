/*
  This script handles smooth navigation from the hero section
  to the intro page when the scroll-down arrow is clicked,
  with enhanced visual transition effects.
*/

document.addEventListener("DOMContentLoaded", function () {
  const scrollArrow = document.querySelector(".scroll-down");

  if (scrollArrow) {
    scrollArrow.addEventListener("click", function () {
      // Add a fade-out effect to the body before redirect
      document.body.classList.add("fade-out");

      // Wait for the animation to finish, then redirect
      setTimeout(() => {
        window.location.href = "intro.html";
      }, 600); // longer delay to match animation
    });
  }
});

