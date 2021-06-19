let comunaSelect = document.getElementById('id_comuna').innerHTML = ''; // Initially comuna select must be empty
let showPwdButton = document.getElementById('show_pwd');
let pwdField = document.getElementById('id_password');
showPwdButton.addEventListener("click", function(){
    if (pwdField.type === 'password') {
        pwdField.type = 'text';
        showPwdButton.className = 'fa fa-eye-slash';
    }
    else {
        pwdField.type = 'password';
        showPwdButton.className = 'fa fa-eye';
    }
})
