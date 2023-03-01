function verification(){
    passwordInput = document.getElementById('passwordInput') 
    rePasswordInput = document.getElementById('rePasswordInput')
    button = document.getElementById('signUpBtn')

    if(passwordInput.value === rePasswordInput.value){
        button.disabled = false
    }else{
        button.disabled = true
    }

}