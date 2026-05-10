// Your solution goes here 
function isStrongPassword(pass){

    if (pass.length < 8){
        return false
    }

   if (pass.indexOf('password') != -1){
        return false;
    }


    for (var i = 0; i < pass.length; i++){
        if (pass.charCodeAt(i) >= 65 && pass.charCodeAt(i) < 90){
            return true
        }
    }

    return false
}