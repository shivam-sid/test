// scrollToIntro.js

/*
  This script handles smooth navigation from the hero section
  to the intro page when the scroll-down arrow is clicked.
*/

document.addEventListener("DOMContentLoaded", function () {
  // Select the scroll-down element (the arrow)
  const scrollArrow = document.querySelector(".scroll-down");

  if (scrollArrow) {
    scrollArrow.addEventListener("click", function () {
      // Add delay for visual flow (optional)
      setTimeout(() => {
        // Redirect to the intro.html page
        window.location.href = "intro.html";
      }, 300); // short delay to match animation timing
    });
  }
});
