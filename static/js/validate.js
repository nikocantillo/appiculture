//Validaciones de email y contraseña
const emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
const passwordRegExp = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,25}$/

function addEvent(element, event, callback) {
  let previousEventCallBack = element["on"+event];
  element["on"+event] = function (e) {
    const output = callback(e);

    // Una devolución de llamada que devuelve «false» detiene la cadena de devolución de llamada
    // e interrumpe la ejecución de la devolución de llamada del evento.
    if (output === false) return false;

    if (typeof previousEventCallBack === 'function') {
      output = previousEventCallBack(e);
      if(output === false) return false;
    }
  }
};




function ValidateRegistro(){
    alert("hola")

    var username = document.getElementById('username').value;
    var names = document.getElementById('fname').value;
    var last_name = document.getElementById('lname').value;
    // var genre = document.getElementById('genre').value;
    var email = document.getElementById('email').value;
    var department = document.getElementById('email').value;
    var city = document.getElementById('pass1').value;
    var phone = document.getElementById('pass1').value;
    var password = document.getElementById('pass1').value;
    var new_password = document.getElementById('pass1').value;

    console.log(email, city, password, new_password)
 

    
    var name_regex = /^[A-Za-z\s]+$/
    var numbers_regex = /^[0-9]+$/
    var email_regex = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/
    var expre = /^(?=[A-Za-z]+[0-9]|[0-9]+[A-Za-z])[A-Za-z0-9]{0,24}$/;


    if (!$("input[name='gender']:checked").val()) {
      document.getElementById("errorGender").innerHTML = '*Campo obligatorio'
       return false;}
    document.getElementById("errorGender").innerHTML = ''

    if(names.length == 0 ){
        document.getElementById("errorName").innerHTML = '*Campo obligatorio'
        return false;
    }
    if(!name_regex.test(names)){
        document.getElementById("errorName").innerHTML = '*Nombre inválido'
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
    if(!name_regex.test(last_name)){
        document.getElementById("errorLastName").innerHTML = '*Apellido o apellidos inválidos'
        return false;
    }
    document.getElementById("errorLastName").innerHTML = ''

    if(last_name.length >50){
        document.getElementById("errorLastName").innerHTML = "Solo se permiten 50 caracteres"
        return false;
    }
    document.getElementById("errorLastName").innerHTML = ''



    // if(genre.length == 0){
    //     document.getElementById("errorGenre").innerHTML = '*Campo obligatorio'
    //     return false;
    // }
    // document.getElementById("errorGenre").innerHTML = ''


    if(email.length == 0){
        document.getElementById("errorEmail").innerHTML = '*Campo obligatorio'
        return false;
    }
    if(!email_regex.test(email)){
      
        document.getElementById("errorEmail").innerHTML = '*Correo inválido'
        document.getElementById("errorPhone").innerHTML = ""
        
        return false;
    }
    document.getElementById("errorEmail").innerHTML = ''



    if(phone.length == 0){
      document.getElementById("errorPhone").innerHTML = '*Campo obligatorio'
      return false;
  }
  document.getElementById("errorPhone").innerHTML = ""
  if(phone.length != 10){
    document.getElementById("errorPhone").innerHTML = 'El numero debe ser de 10 caracteres'
    return false;
}
    document.getElementById("errorPhone").innerHTML = ''
  if(!numbers_regex.test(phone)){
      document.getElementById("errorPhone").innerHTML = '*Número inválido'
      return false;
  }
  document.getElementById("errorPhone").innerHTML = ''


  if(password.length == 0){
      document.getElementById("errorPassword").innerHTML = '*Campo obligatorio'
      return false;
  }
  document.getElementById("errorPassword").innerHTML = ''
  if(email_regex.test(password)){
      document.getElementById("errorPassword").innerHTML = 'Debe ser una contreña entre 6 y 24 carácteres'
      return false;
  }
  document.getElementById("errorPassword").innerHTML = ''

  
  if(new_password != password){
    document.getElementById("errorPassword2").innerHTML = 'Las contraseñas no coinciden'
    return false;
}
document.getElementById("errorPassword2").innerHTML = ''
  if(new_password.length == 0){
      document.getElementById("errorPassword2").innerHTML = '*Campo obligatorio'
      return false;
  }
  document.getElementById("errorPassword2").innerHTML = ''
  if(new_password.length < 6){
      document.getElementById("errorPassword2").innerHTML = 'Debe ser una contreña entre 6 y 24 carácteres'
      return false;
  }
  document.getElementById("errorPassword2").innerHTML = ''
  if(!expre.test(new_password)){
      document.getElementById("errorPassword2").innerHTML = 'Debe contener al menos una letra y un número'
      return false;
  }
  document.getElementById("errorPassword2").innerHTML = ''


    if(department.length == 0){
        document.getElementById("errorDepartment").innerHTML = '*Campo obligatorio'
        return false;
    }
    document.getElementById("errorDepartment").innerHTML = ''


    if(city.length == 0){
        document.getElementById("errorCity").innerHTML = '*Campo obligatorio'
        return false;
    }
    document.getElementById("errorCity").innerHTML = ''


    if (!$("input[name='tipoPapa']:checked").val()) {
      document.getElementById("errorFirst").innerHTML = '*Campo obligatorio'
       return false;
   }
   document.getElementById("errorFirst").innerHTML = ''

  
 

   
  
    document.getElementById('registroButton').click();
    
    



}