window.addEventListener("DOMContentLoaded", (event) => {

    let nav = document.querySelector('nav');
    let link_menu = document.querySelector('.link-menu-mobile');

    document.querySelector('.link-menu-mobile').addEventListener('click', function() {

        if (nav.classList.contains('hero__menu--open')) {
            nav.classList.remove("hero__menu--open");
            link_menu.classList.remove("link-menu-mobile--close");

        } else {
            nav.classList.add("hero__menu--open");
            link_menu.classList.add("link-menu-mobile--close");
        }

    });

});




