document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll(".counter");

    const animateCounter = (counter) => {

        const target = parseInt(counter.dataset.target);
        const duration = 2000;
        const stepTime = 20;
        const increment = target / (duration / stepTime);

        let current = 0;

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {
                counter.textContent = target.toLocaleString();
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current).toLocaleString();
            }

        }, stepTime);

    };

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                animateCounter(entry.target);

                observer.unobserve(entry.target);

            }

        });

    }, {
        threshold: 0.5
    });

    counters.forEach(counter => observer.observe(counter));

});