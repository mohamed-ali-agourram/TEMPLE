const mobile_menu = document.getElementById("mobile-menu"),
    overlay = document.querySelector(".overlay"),
    open = document.getElementById("open"),
    close = document.getElementById("close");



var navscreen


open.addEventListener("click", () => {
    mobile_menu.style.transform = "translateX(0vw)";
    mobile_menu.style.visibility = "visible";
    overlay.style.display = "inherit"
})
overlay.addEventListener("click", () => {
    mobile_menu.style.transform = `translateX(${-navscreen}vw)`;
    mobile_menu.style.visibility = "hidden";
    overlay.style.display = "none";
})

close.addEventListener("click", () => {
    mobile_menu.style.transform = `translateX(${-navscreen}vw)`;
    mobile_menu.style.visibility = "hidden";
    overlay.style.display = "none"
})

const links = document.querySelector(".mobile_nav_filter"),
    open_links = document.getElementById("open-links"),
    close_links = document.getElementById("close-links");

function toggle_links() {
    open_links.classList.toggle("hide")
    close_links.classList.toggle("hide")
}

open_links.addEventListener("click", toggle_links)
open_links.addEventListener("click", () => {
    links.style.display = "flex";
})

close_links.addEventListener("click", toggle_links)
close_links.addEventListener("click", () => {
    links.style.display = "none";
})