$(document).ready(function () {
    var user_owner = true; //server logic
    var config_button = $("#config-button");
    if( user_owner ) {
        config_button.click(function(event) {
            window.location.href='/edit-profile.html' //&id=123'
        });
    }
    else {
        config_button.hide();
    }
});