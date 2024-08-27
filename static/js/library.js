document.addEventListener('DOMContentLoaded', () => {
    const libraryBooks = document.querySelector('.library-books');

    function animateBooks() {
        const bookCards = document.querySelectorAll('.book-card');
        bookCards.forEach((card, index) => {
            card.style.animation = `fadeIn 0.5s ease-in-out ${index * 0.1}s`;
        });
    }

    animateBooks();

    // Add more library-specific functionality here if needed
});