//slider
window.onresize = filter;
window.onload = filter;

var translateBy
const slider = document.querySelector(".slider");


function filter() {
    slider.style.transform = "translate(0%)";
    document.querySelector('.selected').classList.remove('selected')
    document.getElementById("html_li").classList.add('selected');
    width = window.innerWidth;
    if (width <= 786) {
        translateBy = 90
        navscreen = 75
    } else {
        translateBy = 65
        navscreen = 35
    }
}


document.querySelectorAll(".controls li").forEach((indicator, index) => {
    indicator.addEventListener("click", function() {
        document.querySelector('.selected').classList.remove('selected');
        indicator.classList.add('selected');
        slider.style.transform = "translate(" + index * -translateBy + "vw)";
    })
})

//copy code
function copy_code(btn, area, model) {
    const areaBtn = document.querySelector(btn);
    const theArea = document.querySelector(area);
    const span = document.querySelector(model);
    const i = document.querySelectorAll('.fa-copy')
    areaBtn.addEventListener("click", () => {
        theArea.select();
        document.execCommand("copy");
        theArea.setSelectionRange(0, 0);
        theArea.blur();
        areaBtn.style.background = "rgb(89, 219, 89)";
        span.textContent = "Copied";
        i.forEach((x) => {
            x.className = "fa-solid fa-square-check"
        })
        setTimeout(() => {
            areaBtn.style.background = "white"
            span.textContent = "Copy";
            document.querySelectorAll('.fa-square-check').forEach((x) => {
                x.className = "fa-regular fa-copy"
            })
        }, 900)
    })
}
copy_code('.btn_HTML', '.area_HTML', '.span_HTML')
copy_code('.btn_CSS', '.area_CSS', '.span_CSS')
copy_code('.btn_JS', '.area_JS', '.span_JS')