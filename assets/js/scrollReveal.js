// Reveal elements on scroll
document.addEventListener("DOMContentLoaded", () => {
  const reveals = document.querySelectorAll(".reveal");

  const revealOnScroll = () => {
    const triggerPoint = window.innerHeight * 0.85;

    reveals.forEach((el) => {
      const top = el.getBoundingClientRect().top;
      if (top < triggerPoint) {
        el.classList.add("active");
      }
    });
  };

  // Initial + scroll listener
  revealOnScroll();
  window.addEventListener("scroll", revealOnScroll);
});
