const search = document.querySelector(".search_label"),
    open_search = document.getElementById("open_search"),
    close_search = document.getElementById("close_search");

function toggle(elem) {
    if (elem.style.display == "none") {
        elem.style.display = "flex"
    } else {
        elem.style.display = "none"
    }
}

open_search.addEventListener("click", () => toggle(open_search))
open_search.addEventListener("click", () => {
    search.style.visibility = "visible"
    close_search.style.display = "flex"
})
close_search.addEventListener("click", () => toggle(close_search))
close_search.addEventListener("click", () => {
    search.style.visibility = "hidden"
    open_search.style.display = "flex"
})