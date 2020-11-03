var nombre = document.getElementById('Nombre');
var apellido = document.getElementById('apellido');
var gmail = document.getElementById('Gmail');
var telefono = document.getElementById('Telefono');
var Sexo = document.getElementById('Sexo')
var error = document.getElementById('error');
error.style.color='white';




function enviarFormulario(){
    console.log('Enviando Formulario..')


    var mensajeError = [];
    if(nombre.value === null || nombre.value === ''){
        mensajeError.push('Ingresa tu nombre');
    }
    if(apellido.value === null || apellido.value === ''){
        mensajeError.push('Ingresa tu apellido');
    }
    if(gmail.value === null || gmail.value === ''){
        mensajeError.push('Ingresa tu gmail');
    }
    if(telefono.value === null || telefono.value === ''){
        mensajeError.push('Ingresa tu telefono');
    }
    
    error.innerHTML = mensajeError.join(', ')




    return false;
}

