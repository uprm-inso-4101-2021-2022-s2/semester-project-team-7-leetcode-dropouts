const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

const countdown = document.querySelector(".countdown");
const date = new Date(25,00);

console.log(date);

countdown.innerHTML = '<div>${minutes}</div> <div>${seconds}</div>';

menu.addEventListener('click', function(){
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});