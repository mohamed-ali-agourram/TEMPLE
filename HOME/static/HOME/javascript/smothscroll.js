const scroller = document.querySelector(".scroller")
const header = document.querySelector(".header")
let lastScrollY = window.scrollY



window.addEventListener("scroll", () => {
    if (lastScrollY < window.scrollY) {
        scroller.style.visibility = "inherit"
        scroller.style.transform = "translateX(-1vw)";

        if (lastScrollY > 30) {
            header.style.visibility = "hidden"
            header.style.transform = "translateY(-8vh)";

        }
    } else {
        scroller.style.transform = "translateX(10vw)";
        header.style.transform = "translateY(0)";
        scroller.style.visibility = "hidden"
        header.style.visibility = "inherit"
    }
    lastScrollY = window.scrollY;

});