function validar(){
    var validar = emailval();
    if(validar==false){
        return false;
    }
    validar = nameval();
    if(validar==false){
        return false;
    }
    validar = contrval();
    if(validar==false){
        return false;
    }
    return true;
}
function emailval(){
var email = document.getElementById('txtEmail').value;
var quitar = email.trim();
var contar = quitar.length;
if(contar<6){
    error = "Mínimo 6 caracteres para el email.";
    document.getElementById('error').innerHTML = error;
    return false;
}
return true;
}
function nameval(){
var name_user = document.getElementById('txtNombre').value;
var quitar = name_user.trim();
var num_user = quitar.length;
if(num_user < 3 || num_user >30){
    error_1 = "";
    error = "Mínimo 3 caracteres para el nombre y máximo 30 caracteres.";
    document.getElementById('error').innerHTML = error_1;
    document.getElementById('error_2').innerHTML = error;
    return false;
}
return true;
}
function contrval(){
    var pass_user = document.getElementById('txtPasslog').value;
    var quitar = pass_user.trim();
    var num_pass = quitar.length;
    if(num_pass < 8 || num_pass >30){
        error_1 = "";
        error = "Mínimo 8 caracteres para la contraseña y máximo 30 caracteres.";
        document.getElementById('error').innerHTML = error_1;
        document.getElementById('error_2').innerHTML = error_1;
        document.getElementById('error_3').innerHTML = error;
        return false;
    }
    return true;
}