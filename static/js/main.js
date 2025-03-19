// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.querySelector('input[name="stars_given"]');
    let rating = 0;

    stars.forEach(star => {
        star.addEventListener('mouseover', () => {
            resetStars();
            highlightStars(star.dataset.value);
        });

        star.addEventListener('click', () => {
            rating = star.dataset.value;
            ratingInput.value = rating;
        });

        star.addEventListener('mouseout', () => {
            resetStars();
            if (rating) {
                highlightStars(rating);
            }
        });
    });

    function resetStars() {
        stars.forEach(star => {
            star.classList.remove('selected');
        });
    }

    function highlightStars(n) {
        for (let i = 0; i < n; i++) {
            stars[i].classList.add('selected');
        }
    }
});
