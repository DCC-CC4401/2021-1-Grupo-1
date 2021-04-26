$(document).ready(function () {
    $("#filterLink").click(function () {
        $("#filterContainer").fadeToggle(300);
        return false;
    });

//Document Click hiding the popup
    $(document).click(function (event) {
        if($(event.target).attr('class') === undefined ) {
            $("#filterContainer").hide();
        }
        else if(!($(event.target).attr('class').includes("filterOption"))){
                $("#filterContainer").hide();
        }
    });

// Popup click
$("#notificationContainer").click(function(event) {
    if (event !== undefined){
    event.stopPropagation();
    }
});

});