$(document).ready(function () {
   window.addEventListener("resize", function(event) {
    console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
  })
  window.onscroll = function () {
    myFunction()

  };

  const navbar = document.getElementById("navbar");
  const sticky = navbar.offsetTop;

  function myFunction() {
    if (window.pageYOffset >= sticky) {
      navbar.classList.add("sticky")
    } else {
      navbar.classList.remove("sticky");
    }
  }



});

