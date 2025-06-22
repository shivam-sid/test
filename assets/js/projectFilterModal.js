document.addEventListener('DOMContentLoaded', (event) => {
    // --- Get DOM Elements ---
    const projectCards = document.querySelectorAll('.project-card'); // All clickable project cards
    const filterButtons = document.querySelectorAll('.filter-button'); // All filter buttons
    const projectPopupModal = document.getElementById('project-popup-modal'); // The modal container
    const modalContentArea = projectPopupModal.querySelector('.modal-content-area'); // Area to load dynamic content
    const modalBackdrop = document.getElementById('modal-backdrop'); // The overlay behind the modal
    const body = document.body; // The <body> element for scroll control
    const closeButton = projectPopupModal.querySelector('.close-button'); // The modal's close button

    // Elements for page load animation
    const mainContent = document.querySelector('main'); // The main content area that contains filters and grid

    // --- Project Filtering Functions ---

    /**
     * Filters the project cards based on the selected category.
     * @param {string} filterCategory - The category to filter by (e.g., 'web-development', 'all').
     */
    function filterProjects(filterCategory) {
        projectCards.forEach(card => {
            const categories = card.dataset.category ? card.dataset.category.split(' ') : [];
            const isMatch = filterCategory === 'all' || categories.includes(filterCategory);
            
            if (isMatch) {
                card.classList.remove('hidden');
                // Optional: Re-trigger animation or just make visible if desired
                card.style.display = 'block'; // Or 'grid', depends on card display
                card.style.opacity = '1';
                card.style.transform = 'scale(1)';
            } else {
                card.classList.add('hidden');
                card.style.display = 'none'; // Completely hide from layout
            }
        });
    }

    // --- Modal Functions ---

    /**
     * Fetches HTML content for a specific project and injects it into the modal.
     * @param {string} projectId - The unique ID of the project (e.g., 'the-surf-project').
     */
    async function loadProjectContent(projectId) {
        const contentUrl = `projects-content/${projectId}.html`; // Path to the HTML content file

        try {
            // Display a loading message while fetching
            modalContentArea.innerHTML = '<p style="text-align: center; padding: 20px;">Loading project details...</p>';
            
            const response = await fetch(contentUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const htmlContent = await response.text();
            modalContentArea.innerHTML = htmlContent; // Inject the fetched HTML
        } catch (error) {
            console.error(`Failed to load project content for ID "${projectId}":`, error);
            modalContentArea.innerHTML = '<p style="text-align: center; color: red; padding: 20px;">Failed to load project details. Please try again later.</p>';
        }
    }

    /**
     * Opens the project modal and its backdrop, loading specified project content.
     * @param {string} projectId - The ID of the project to load and display.
     */
    function openProjectModal(projectId) {
        loadProjectContent(projectId); // Load content for the specified project
        
        projectPopupModal.classList.add('is-visible'); // Show modal
        modalBackdrop.classList.add('is-visible');     // Show backdrop
        body.classList.add('modal-open');              // Prevent body scrolling
    }

    /**
     * Closes the project modal and its backdrop.
     */
    function closeProjectModal() {
        projectPopupModal.classList.remove('is-visible'); // Hide modal
        modalBackdrop.classList.remove('is-visible');     // Hide backdrop
        body.classList.remove('modal-open');              // Re-enable body scrolling
        // Optional: Clear modal content when closed to save memory/prevent flicker
        // setTimeout(() => { modalContentArea.innerHTML = ''; }, 300); 
    }

    // --- Event Listeners ---

    // 1. Listen for clicks on each project card to open the modal
    projectCards.forEach(card => {
        // Initially hide/blur cards via inline style for the page load animation
        card.style.opacity = '0';
        card.style.filter = 'blur(5px)';

        card.addEventListener('click', function() {
            const projectId = this.dataset.projectId; // Get the project ID from the clicked card
            openProjectModal(projectId); // Open the modal with this project's content
        });
    });

    // 2. Listen for close button click within the modal
    closeButton.addEventListener('click', closeProjectModal);

    // 3. Listen for clicks on the backdrop (to close the modal)
    modalBackdrop.addEventListener('click', closeProjectModal);

    // 4. Optional: Close modal on Escape key press
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && projectPopupModal.classList.contains('is-visible')) {
            closeProjectModal();
        }
    });

    // 5. NEW: Listen for clicks on filter buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove 'active' class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add 'active' class to the clicked button
            this.classList.add('active');

            const filterCategory = this.dataset.filter; // Get the filter category (e.g., 'web-development')
            filterProjects(filterCategory); // Apply the filter
        });
    });

    // --- Page Load Animations with Blur ---

    // Initially hide/blur the main content area via inline style
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.filter = 'blur(8px)';
    }

    // After a delay, remove inline styles and add CSS animation classes
    setTimeout(() => {
        if (mainContent) {
            mainContent.style.opacity = ''; // Remove inline opacity
            mainContent.style.filter = ''; // Remove inline blur
            // Add the class to the body that triggers the main content animation via CSS
            body.classList.add('fade-in-on-load'); 
        }

        // Staggered animation for individual project cards
        // Apply initial filter (usually 'all') after cards are animated
        projectCards.forEach((card, index) => {
            setTimeout(() => {
                card.style.opacity = ''; // Remove inline opacity
                card.style.filter = ''; // Remove inline blur
                card.classList.add('fade-in-card'); // Add class to trigger card animation
                
                // Ensure initial 'all' filter is applied after cards are visible
                if (index === projectCards.length - 1) {
                    filterProjects('all'); // Apply 'all' filter once all cards have been processed
                }
            }, index * 120); // Stagger each card's animation by 120ms
        });

    }, 200); // Overall delay before starting ALL page load animations
});