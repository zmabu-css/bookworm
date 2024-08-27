document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.querySelector('form');
    const searchInput = document.querySelector('input[name="query"]');
    const searchResults = document.querySelector('.search-results');

    searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
            fetchSearchResults(query);
        }
    });

    function fetchSearchResults(query) {
        fetch(`/search?query=${encodeURIComponent(query)}`)
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newResults = doc.querySelector('.search-results');
                searchResults.innerHTML = newResults.innerHTML;
                animateResults();
            })
            .catch(error => console.error('Error fetching search results:', error));
    }

    function animateResults() {
        const bookCards = document.querySelectorAll('.book-card');
        bookCards.forEach((card, index) => {
            card.style.animation = `fadeIn 0.5s ease-in-out ${index * 0.1}s`;
        });
    }
});