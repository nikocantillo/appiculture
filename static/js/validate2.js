// define lo que sucede cuando el usuario intenta enviar los datos.
console.log('holaaaaaaaaaaaaaaaaa')
const form1 = document.getElementById('registerForm')
var username = document.getElementById('username').value;
var names = document.getElementById('fname').value;
var last_name = document.getElementById('lname').value;
// var genre = document.getElementById('genre').value;
var email = document.getElementById('email').value;
var password = document.getElementById('pass1').value;
var new_password = document.getElementById('pass1').value;


function addEvent(element, event, callback) {
    let previousEventCallBack = element["on"+event];
    element["on"+event] = function (e) {
      const output = callback(e);
      if (output === false) return false
      if (typeof previousEventCallBack === 'function') {
        output = previousEventCallBack(e);
        if(output === false) return false;
      }
    }
  };


addEvent(form1, "submit", function () {
    if(username.length > 0){
        document.getElementById("errorUserName").innerHTML = '*Campo obligatorio'
        return false;
    }
    document.getElementById("errorUserName").innerHTML = ''
    if(username.length > 20){
        document.getElementById("errorUserName").innerHTML = '*Solo se permiten 20 caracteres'
        return false;
    }
    document.getElementById("errorUserName").innerHTML = ''
    if(names.length == 0){
        document.getElementById("errorName").innerHTML = '*Campo obligatorio'
        return false;
    }
    document.getElementById("errorName").innerHTML = ''
    if(names.length >50){
        document.getElementById("errorName").innerHTML = 'Solo se permiten 50 caracteres '
        return false;
    }
    document.getElementById("errorName").innerHTML = ''

    if(last_name.length == 0){
        document.getElementById("errorLastName").innerHTML = '*Campo obligatorio'
        return false;
    }
    document.getElementById("errorLastName").innerHTML = ''
  
    if (Nuip.value.length > 12) {
      document.getElementById('errornuip').innerHTML="Se permiten máximo 12 caracteres."
      return false;
    } 
      document.getElementById('errornuip').innerHTML=""
    
    
    if (names.value.length > 50) {
      document.getElementById('errorname').innerHTML="Se permiten máximo 50 caracteres."
      return false;
    } 
      document.getElementById('errorname').innerHTML=""
    
    
    if (lastnames.value.length > 50) {
      errorLastname.innerHTML="Se permiten máximo 50 caracteres."
      return false;
    } else {
      errorLastname.innerHTML=""
    }
  
    if (fechas2 < Date.now() && yanacio.checked === false) {
      errorParto.innerHTML="Fecha invalida de parto."
      return false;
    } else {
      errorParto.innerHTML=""
    }
    if(password.length < 6){
        document.getElementById("errorPassword").innerHTML = 'Debe ser una contreña entre 6 y 24 carácteres'
        return false;
    }
    document.getElementById("errorPassword").innerHTML = ''
    if(new_password.length < 6){
        document.getElementById("errorPassword2").innerHTML = 'Debe ser una contreña entre 6 y 24 carácteres'
        return false;
    }
    document.getElementById("errorPassword2").innerHTML = ''
  
  
  
    // else {
    //   errorParto.innerHTML=""
    //   errorNuip.innerHTML=""
    //   errorNames.innerHTML=""
    //   errorLastname.innerHTML=""
    // }
  
    
  });
  