// Solo se muestra el primer input
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