document.addEventListener("DOMContentLoaded", function () {
    // --- Navbar Toggle Logic ---
    const navToggle = document.querySelector(".nav-toggle");
    const navMenu = document.querySelector(".nav-menu");

    if (navToggle && navMenu) {
        navToggle.addEventListener("click", () => {
            navMenu.classList.toggle("show");
            navToggle.querySelector('i').classList.toggle('fa-bars');
            navToggle.querySelector('i').classList.toggle('fa-times'); // Change icon
        });

        // Close menu if a link is clicked (for single-page navigation)
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) { // Only close on mobile
                    navMenu.classList.remove('show');
                    navToggle.querySelector('i').classList.remove('fa-times');
                    navToggle.querySelector('i').classList.add('fa-bars');
                }
            });
        });
    }

    // --- Project Filter and Modal Logic ---
    const filterButtons = document.querySelectorAll(".filter-btn");
    const projectCards = document.querySelectorAll(".project-card");
    const modal = document.getElementById("projectModal");
    const modalImg = document.getElementById("modal-img");
    const modalTitle = document.getElementById("modal-title");
    const modalDesc = document.getElementById("modal-description");
    const closeModalBtn = document.querySelector(".modal-close");
    const nextBtn = document.getElementById("nextProject");
    const prevBtn = document.getElementById("prevProject");

    let currentIndex = 0;
    let displayedCards = []; // Store currently displayed cards after filtering
    let lastScrollY = 0; // Variable to store the scroll position

    // Function to calculate scrollbar width dynamically
    function getScrollbarWidth() {
        const outer = document.createElement('div');
        outer.style.visibility = 'hidden';
        outer.style.overflow = 'scroll';
        outer.style.msOverflowStyle = 'scrollbar';
        document.body.appendChild(outer);

        const inner = document.createElement('div');
        outer.appendChild(inner);

        const scrollbarWidth = (outer.offsetWidth - inner.offsetWidth);

        outer.parentNode.removeChild(outer);
        return scrollbarWidth;
    }

    // Set CSS variable for scrollbar width once
    // Using requestAnimationFrame to ensure DOM is ready for measurement
    requestAnimationFrame(() => {
        document.documentElement.style.setProperty('--scrollbar-width', `${getScrollbarWidth()}px`);
    });


    function updateDisplayedCards() {
        // Only include visible cards (those not hidden by display:none)
        displayedCards = Array.from(projectCards).filter(card => window.getComputedStyle(card).display !== 'none');
    }

    // Filter logic
    filterButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            document.querySelector(".filter-btn.active")?.classList.remove("active");
            btn.classList.add("active");

            const filter = btn.getAttribute("data-filter");

            projectCards.forEach((card) => {
                const categories = card.getAttribute("data-category").split(" ");
                // Set display to 'block' if it matches filter, else 'none'
                card.style.display = (filter === "all" || categories.includes(filter)) ? "block" : "none";
            });

            updateDisplayedCards(); // Update displayedCards array after filtering
            currentIndex = 0; // Reset index to first visible card
            if (displayedCards.length === 0) {
                currentIndex = -1; // No cards to display
            }
        });
    });

    // Modal trigger
    projectCards.forEach((card) => {
        card.addEventListener("click", () => {
            updateDisplayedCards(); // Ensure displayedCards is up-to-date
            const visibleIndex = displayedCards.indexOf(card);
            if (visibleIndex !== -1) { // Only open if the clicked card is currently visible
                openModal(visibleIndex);
            }
        });
    });

    // Open modal
    function openModal(index) {
        if (displayedCards.length === 0 || index < 0 || index >= displayedCards.length) {
            return; // No cards to show or index out of bounds
        }

        const card = displayedCards[index];
        const img = card.querySelector("img");
        const title = card.querySelector("h3");
        const desc = card.querySelector("p");

        modalImg.src = img.src;
        modalTitle.textContent = title.textContent;
        modalDesc.textContent = desc.textContent;

        // --- Crucial Scroll Lock ---
        lastScrollY = window.scrollY; // Store current scroll position

        // Apply styles to html and body to prevent scroll jump and lock it
        document.documentElement.classList.add('modal-active'); // Add to html
        document.body.classList.add('modal-active'); // Add to body (for scrollbar compensation)

        // Directly set styles on body for precise control over scroll lock
        document.body.style.position = 'fixed';
        document.body.style.top = `-${lastScrollY}px`; // Shift body content up to match scroll
        document.body.style.width = '100%'; // Maintain body width

        // Display modal and trigger animation
        modal.style.display = "flex";
        requestAnimationFrame(() => {
            modal.classList.add("modal-show");
        });

        currentIndex = index; // Update current index for navigation
    }

    // Close modal
    function closeModal() {
        modal.classList.remove("modal-show"); // Trigger slide-out animation

        // Re-enable body scroll and restore position after animation completes
        setTimeout(() => {
            modal.style.display = "none"; // Hide after animation completes

            // --- Crucial Scroll Unlock ---
            // Remove styles from html and body
            document.documentElement.classList.remove('modal-active');
            document.body.classList.remove('modal-active'); // For scrollbar compensation

            // Restore body styles (important to remove them)
            document.body.style.position = '';
            document.body.style.top = '';
            document.body.style.width = '';

            // Restore scroll position
            window.scrollTo(0, lastScrollY);
        }, 300); // Matches the transition/animation duration for closing
    }

    closeModalBtn.addEventListener("click", closeModal);

    // Close when clicking outside the modal content
    window.addEventListener("click", (e) => {
        // Check if the click target is the modal backdrop itself, not content within
        if (e.target === modal) {
            closeModal();
        }
    });

    // Keyboard navigation and close
    document.addEventListener("keydown", (e) => {
        if (modal.classList.contains("modal-show")) { // Check if modal is currently open and animating
            if (e.key === "ArrowRight") {
                currentIndex = (currentIndex + 1) % displayedCards.length;
                openModal(currentIndex);
            } else if (e.key === "ArrowLeft") {
                currentIndex = (currentIndex - 1 + displayedCards.length) % displayedCards.length;
                openModal(currentIndex);
            } else if (e.key === "Escape") {
                closeModal();
            }
        }
    });

    // Touch swipe down to close
    let touchStartY = 0;
    let touchEndY = 0;

    modal.addEventListener("touchstart", (e) => {
        if (e.changedTouches && e.changedTouches[0]) {
            touchStartY = e.changedTouches[0].screenY;
        }
    }, { passive: true }); // Use passive to avoid performance issues

    modal.addEventListener("touchend", (e) => {
        if (e.changedTouches && e.changedTouches[0]) {
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }
    });

    function handleSwipe() {
        if (touchStartY === 0 && touchEndY === 0) return;

        const swipeThreshold = 50; // Pixels
        if (touchEndY > touchStartY + swipeThreshold) { // Swipe down to close
            closeModal();
        }
        touchStartY = 0;
        touchEndY = 0;
    }

    // Next/Previous buttons in modal
    nextBtn?.addEventListener("click", () => {
        if (displayedCards.length > 0) { // Ensure there are cards to navigate
            currentIndex = (currentIndex + 1) % displayedCards.length;
            openModal(currentIndex);
        }
    });

    prevBtn?.addEventListener("click", () => {
        if (displayedCards.length > 0) { // Ensure there are cards to navigate
            currentIndex = (currentIndex - 1 + displayedCards.length) % displayedCards.length;
            openModal(currentIndex);
        }
    });

    // Initial call to populate displayedCards based on default filter (all)
    updateDisplayedCards();
});