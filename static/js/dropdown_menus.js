$(document).ready(function (){
    attachDropdownListeners("#filterLink", "#filterContainer");
    attachDropdownListeners("#notificationLink", "#notificationContainer");
    attachDropdownListeners("#optionLink", "#optionContainer");
})

function isDescendantOrEqual(a, b) {
  // Checks if b is descendant or equal to a
  return ( a.has(b).length >= 1 ) || a.is(b);
}

function attachDropdownListeners (idButton, idContainer){
    $(document).ready(function (){
        let container =  $(idContainer);
        $(idButton).click(function () {
            container.fadeToggle(300);
        });

        $(document).click(function (event) {
            if((isDescendantOrEqual(container, $(event.target)) || $(event.target).is(idButton))){
                return null;
            }
             container.hide();
        });
    });
}