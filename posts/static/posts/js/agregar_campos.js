let status = document.getElementById("id_status");
let fecha = document.getElementsByClassName("form-group")[12];

// Se oculta por defecto el campo de fecha y se le agrega un listener
// al campo de status del animal
fecha.style.display = "none";
status.addEventListener("change", mostrarFecha);

// Se muestra o no el campo de fecha de avistamiento
function mostrarFecha() {
    if (status.selectedIndex === 0 || status.selectedIndex === 1) {
        fecha.style.display = "none";
    } else if (status.selectedIndex === 2) {
        fecha.style.display = "block";
    }
}

// Solo se muestra el primer input de imagen
document.getElementById("id_form-0-image").style.display = "block";

// Se le agrega un listener a los 3 primeros inputs
// El último no porque no debería efectuar ninguna acción
document.getElementById("id_form-0-image").addEventListener("click", mostrarInputs);
document.getElementById("id_form-1-image").addEventListener("click", mostrarInputs);
document.getElementById("id_form-2-image").addEventListener("click", mostrarInputs);

// Se muestra el siguiente input
inputs = 1;
function mostrarInputs() {
    let id_input = "id_form-" + (inputs++) + "-image";
    document.getElementById(id_input).style.display = "block";
}