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

const AddTaskBtn = document.querySelector(".task__btn");

AddTaskBtn.addEventListener("click", myFunction());


function myFunction() {
  let input = prompt("Please Enter Task", "");
  if(input != null){
    document.getElementById("InputAdded").innerHTML = input;
    let Date= prompt("Enter Due Date: ");
    if(Date !=null ){
      document.getElementById("Date").innerHTML = Date;
      let rating = prompt("Importance Rating: ");
      if(rating != null){
        document.getElementById("Rating").innerHTML = rating;
      }
    }

  }
}