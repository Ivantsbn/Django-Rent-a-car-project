let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active')
}

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active')
}

const sr = ScrollReveal ({
    distance: '60px',
    duration: 2500,
    delay: 400,
    reset: true
})
sr.reveal('.text',{delay: 100, origin: 'top'})
sr.reveal('.btn2',{delay: 500, origin: 'left'})
sr.reveal('.home .carhomeimg',{delay: 500, origin: 'left'})
sr.reveal('.ride',{delay: 500, origin: 'top'})
sr.reveal('.services-container',{delay: 500, origin: 'top'})
sr.reveal('.about-container',{delay: 100, origin: 'top'})
sr.reveal('.reviews-container',{delay: 100, origin: 'top'})
sr.reveal('.newsletter .box',{delay: 100, origin: 'bottom'})