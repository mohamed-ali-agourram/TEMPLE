const slideContainer = document.querySelector('.slider_content');
const slide = document.querySelector('.slides');
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');
const interval = 5000;

let slides = document.querySelectorAll('.slide');
let index = 1;
let slideId;

const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slides.length - 1].cloneNode(true);

firstClone.id = 'first-clone';
lastClone.id = 'last-clone';

slide.append(firstClone);
slide.prepend(lastClone);


slide.style.transform = `translateX(${-translateWith * index}vw)`;


const startSlide = () => {
    slideId = setInterval(() => {
        moveToNextSlide();
    }, interval);
};

const getSlides = () => document.querySelectorAll('.slide');

window.onresize = sliderScreenTranslate;
window.onload = sliderScreenTranslate;

var translateWith

function sliderScreenTranslate() {
    var width = window.innerWidth;
    if (width <= 768) {
        translateWith = 95

    } else {
        translateWith = 70
    }
    if (width <= 480) {
        navscreen = 60
    } else {
        navscreen = 35
    }
    slide.style.transform = `translateX(${-translateWith * 1}vw)`;
}

slide.addEventListener('transitionend', () => {
    slides = getSlides();
    if (slides[index].id === firstClone.id) {
        slide.style.transition = 'none';
        index = 1;
        slide.style.transform = `translateX(${-translateWith * index}vw)`;

    }

    if (slides[index].id === lastClone.id) {
        slide.style.transition = 'none';
        index = slides.length - 2;
        slide.style.transform = `translateX(${-translateWith * index}vw)`;
    }
});

const moveToNextSlide = () => {
    slides = getSlides();
    if (index >= slides.length - 1) return;
    index++;
    slide.style.transition = '.7s ease-out';
    slide.style.transform = `translateX(${-translateWith * index}vw)`;
};

const moveToPreviousSlide = () => {
    if (index <= 0) return;
    index--;
    slide.style.transition = '.7s ease-out';
    slide.style.transform = `translateX(${-translateWith * index}vw)`;
};

slideContainer.addEventListener('mouseenter', () => {
    clearInterval(slideId);
});

slideContainer.addEventListener('mouseleave', startSlide);
nextBtn.addEventListener('click', moveToNextSlide);
prevBtn.addEventListener('click', moveToPreviousSlide);

startSlide();