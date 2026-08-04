document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".hero-slide");

    if (!slides.length) return;

    let current = 0;

    function showSlide(index) {

        slides.forEach((slide, i) => {

            if (i === index) {
                slide.classList.add("active");
            } else {
                slide.classList.remove("active");
            }

        });

    }

    showSlide(current);

    setInterval(() => {

        current++;

        if (current >= slides.length) {
            current = 0;
        }

        showSlide(current);

    }, 5000);

});