/*
  Script: projectFilterModal.js
  Description: Handles project filtering and modal popup with animation + swipe + keyboard navigation + button support
*/

document.addEventListener("DOMContentLoaded", function () {
  // Select DOM elements
  const filterButtons = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");
  const modal = document.getElementById("projectModal");
  const modalImg = document.getElementById("modal-img");
  const modalTitle = document.getElementById("modal-title");
  const modalDesc = document.getElementById("modal-description");
  const closeModalBtn = document.querySelector(".modal-close");
  const nextBtn = document.getElementById("nextProject");
  const prevBtn = document.getElementById("prevProject");
  let currentIndex = 0; // Tracks current modal index

  // Filtering functionality
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelector(".filter-btn.active").classList.remove("active");
      btn.classList.add("active");

      const filter = btn.getAttribute("data-filter");

      projectCards.forEach((card) => {
        const categories = card.getAttribute("data-category").split(" ");
        if (filter === "all" || categories.includes(filter)) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  });

  // Modal open functionality
  projectCards.forEach((card, index) => {
    card.addEventListener("click", () => {
      openModal(index);
    });
  });

  // Open modal and populate content
  function openModal(index) {
    const card = projectCards[index];
    const img = card.querySelector("img");
    const title = card.querySelector("h3");
    const desc = card.querySelector("p");

    modal.classList.remove("modal-show");
    setTimeout(() => {
      modalImg.src = img.src;
      modalTitle.textContent = title.textContent;
      modalDesc.textContent = desc.textContent;
      modal.classList.add("modal-show");
    }, 100);

    modal.style.display = "flex";
    document.body.style.overflow = "hidden";
    currentIndex = index;
  }

  // Close modal with close button
  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  });

  // Close modal on outside click
  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });

  // Keyboard navigation: left/right arrow and escape
  document.addEventListener("keydown", function (e) {
    if (modal.style.display === "flex") {
      if (e.key === "ArrowRight") {
        currentIndex = (currentIndex + 1) % projectCards.length;
        openModal(currentIndex);
      } else if (e.key === "ArrowLeft") {
        currentIndex = (currentIndex - 1 + projectCards.length) % projectCards.length;
        openModal(currentIndex);
      } else if (e.key === "Escape") {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
      }
    }
  });

  // Swipe support for mobile
  let touchStartX = 0;
  let touchEndX = 0;

  // Record start position
  modal.addEventListener("touchstart", function (e) {
    touchStartX = e.changedTouches[0].screenX;
  });

  // Record end position and handle swipe direction
  modal.addEventListener("touchend", function (e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  });

  // Detect swipe direction and navigate modal
  function handleSwipe() {
    if (touchEndX < touchStartX - 50) {
      currentIndex = (currentIndex + 1) % projectCards.length;
      openModal(currentIndex);
    }
    if (touchEndX > touchStartX + 50) {
      currentIndex = (currentIndex - 1 + projectCards.length) % projectCards.length;
      openModal(currentIndex);
    }
  }

  // Button navigation support
  nextBtn.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % projectCards.length;
    openModal(currentIndex);
  });

  prevBtn.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + projectCards.length) % projectCards.length;
    openModal(currentIndex);
  });
});
