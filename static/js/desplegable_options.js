$(document).ready(function () {
    $("#optionLink").click(function () {
        $("#optionContainer").fadeToggle(300);
        return false;
    });

//Document Click hiding the popup
    $(document).click(function () {
        $("#optionContainer").hide();
    });

// Popup click
    $("#optionContainer").click(function (event) {
        if (event !== undefined){
        event.stopPropagation();
        }
    });
});