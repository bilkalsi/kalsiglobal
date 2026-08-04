document.addEventListener("DOMContentLoaded", () => {

    // Navbar shadow
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 40) {
            navbar.classList.add("shadow");
        } else {
            navbar.classList.remove("shadow");
        }
    });

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                e.preventDefault();

                window.scrollTo({
                    top: target.offsetTop - 70,
                    behavior: "smooth"
                });
            }

        });
    });

    // Auto close mobile menu
    document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {
        link.addEventListener("click", () => {

            const menu = document.querySelector(".navbar-collapse");

            if (menu.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(menu).hide();
            }

        });
    });

});