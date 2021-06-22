function solicitudt(){
    var validar = correo();
    if(validar==false){
        return false;
    }
    validar = telefono();
    if(validar==false){
        return false;
    }
    validar = descripcion();
    if(validar==false){
        return false;
    }
    return true;
}
function solicituda(){
    var validar = correo();
    if(validar==false){
        return false;
    }
    validar = telefono();
    if(validar==false){
        return false;
    }
    validar = descripcion();
    if(validar==false){
        return false;
    }
    return true;
}
function correo(){
    var email = document.getElementById('txtEmail').value;
    var vacio = email.trim();
    var contable = vacio.length;
    if(contable<6){
        var error = "Su email no puede tener menos de 6 caracteres.";
        document.getElementById('error_0').innerHTML = error;
        return false;
    }
    document.getElementById('error_0').innerHTML = "";    
    return true;
}
function telefono(){
var tel_user = document.getElementById('txtTel').value;
var num_tel = tel_user.length;
if(num_tel<8 || num_tel>8){
    var error = "Inserte 8 digítos. ";
    document.getElementById('error_1').innerHTML = error;
    return false;
}
for (let index = 0; index <= num_tel ; index++) {
    var cont = 0;
    var caracter = tel_user.slice(index,index+1);
    if(caracter == 1){
        cont = cont+1;
    }
    else if(caracter == 2){
        cont = cont+1;
    }
    else if(caracter == 3){
        cont = cont+1;
    }
    else if(caracter == 4){
        cont = cont+1;
    }
    else if(caracter == 5){
        cont = cont+1;
    }
    else if(caracter == 6){
        cont = cont+1;
    }
    else if(caracter == 7){
        cont = cont+1;
    }
    else if(caracter == 8){
        cont = cont+1;
    }
    else if(caracter == 9){
        cont = cont+1;
    }
    else if(caracter == 0){
        cont = cont+1;
    }
    else{
        var error = "No inserte caracteres, solamente números. ";
        document.getElementById('error_1').innerHTML = error;
        index = num_tel+1;
        return false;
    }
}
document.getElementById('error_1').innerHTML = "";
return true;
}
function descripcion(){
    var desc = document.getElementById('txtDesc').value;
    var vacio = desc.trim();
    var contable = vacio.length;
    if(contable>350 || contable<10){
        var error = "Su descripción no puede superar los 350 caracteres, ni tener menos de 10 caracteres.";
        document.getElementById('error_2').innerHTML = error;
        return false;
    }
    document.getElementById('error_2').innerHTML = "";    
    return true;
}
