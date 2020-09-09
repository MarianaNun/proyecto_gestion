$(document).ready(
  function() {
  $('.message a').click(function(){
     $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
  });

$('#show-sign-in').click(function(){
	console.log("Mostrar")
	document.getElementById('register').style.display="none";
	document.getElementById('login').style.display="block";
});

function show(){
	document.getElementById('login').style.display="none";
	document.getElementById('register').style.display="block";
};

function myFunction(x) {
    x.classList.toggle("change");
};

//let miImage = document.getElementsByClassName('imagen')
$('.imagen').click(function(){
    let miSrc = this.src;
    console.log(miSrc)
    if (miSrc.includes('card1.jpg')) {
      this.setAttribute('src','/static/images/card2.jpg');
    } else {
      this.setAttribute('src', '/static/images/card3.jpg');
    }
});


let miImage = document.getElementById('imagen')
miImage.addEventListener('click', function (){
    let miSrc = miImage.src;
    console.log(miSrc)
    if (miSrc.includes('card1.jpg')) {
      miImage.setAttribute('src','/static/images/card2.jpg');
    } else {
      miImage.setAttribute('src', '/static/images/card3.jpg');
    }
});

//Version 2
$('.imagen').click( function (){
    let miSrc = this.src;
    console.log(miSrc)
    if (miSrc.includes('card1.jpg')) {
      this.setAttribute('src','/static/images/card2.jpg');
    } else {
      this.setAttribute('src', '/static/images/card3.jpg');
    }
});

function createParagraph() {
  let para = document.createElement('p');
  para.textContent = 'You clicked the button!';
  document.body.appendChild(para);
};

function confirmacion() {
  var pregunta = confirm("¿Deseas visitar la página principal?")
  if (pregunta){
    alert("Te envío allí rápidamente")
    window.location = "https://norfipc.com/";
  }
  else{
    alert("Quizás en otro momento...\n Gracias de todas formas")
  };
}

$('#imagen3').hover( function (){
    $('#imagen3').hide(200)
});

$('.caja').hover(function(){
    $('.texto').hide();
}, function(){
    $('.texto').show();
});

var btn = document.querySelector('button .className');
var txt = document.querySelector('p  #id');

btn.addEventListener('click', updateBtn);

function updateBtn() {
  if (btn.textContent === 'Iniciar máquina') {
    btn.textContent = 'Detener máquina';
    txt.textContent = 'La máquina se inició!';
  } else {
    btn.textContent = 'Iniciar máquina';
    txt.textContent = 'La máquina se detuvo.';
  }
}






})

