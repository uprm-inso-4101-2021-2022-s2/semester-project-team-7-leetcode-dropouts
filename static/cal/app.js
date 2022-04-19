const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

const countdown = document.querySelector(".countdown");

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

var x = null;
function timer() {

    // if(document.getElementById('pomodoro_button').innerHTML == "START"){
    // Get todays time plus 25 min (1500 seconds * 1000 for the ms)
    var countDownDate = new Date().getTime() + 1501 * 1000;
    // running = true;
    // Update the count down every 1 second
    x = setInterval(function() {

    // Get today's date and time
    var now = new Date().getTime();
                            
    // Find the distance between now and the count down date
    var distance = countDownDate - now;
        
    // Time calculations minutes and seconds
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
    // Output the result in an element with id="displayPomodoro"
    document.getElementById('notDead').innerHTML = minutes + "m " + seconds + "s ";
    document.getElementById('displayPomodoro').style.visibility = "visible";
    document.getElementById('pomodoro_button').style.visibility = "hidden";
        
    // If the count down is over, write Times Up
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("displayPomodoro").innerHTML = "Times Up";
        //document.getElementById('displayPomodoro').style.visibility = "hidden";
    }
    }, 1000);
}
function stopTimer(){
    running = false;
    clearInterval(x)
    //document.getElementById("displayPomodoro").innerHTML = "Stopped";
    document.getElementById('notDead').innerHTML = "25m 0s"
    document.getElementById('displayPomodoro').style.visibility = "visible";
    document.getElementById('pomodoro_button').style.visibility = "visible";
}