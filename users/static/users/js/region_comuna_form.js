let regionSelect = document.getElementById('id_region');
let comunaSelect = document.getElementById('id_comuna');
regionSelect.addEventListener("change", function () {
    // Fetch all comunas associated with current region using /api/get_comunas
    let regionId =  regionSelect.value;
    let comunaId = parseInt(comunaSelect.value);
    if (regionId === "") {
        return;
    }
    fetch('/api/get_comunas/' + regionId)
        .then(response => response.json())
        .then(function(comunas) {
            // Clear comunaSelect and add all new options
            comunaSelect.innerHTML = '';
            comunas.forEach(function(comuna){
                var option = document.createElement('option');
                option.value = comuna.id;
                if(comunaId === comuna.id){
                    option.selected = true;
                }
                option.text = comuna.name;
                comunaSelect.add(option);
            })
        })
        .catch(function(error) {
            console.error('There was a problem fetching comunas for regionId = ' + regionId + ':' + error.message);
        })
})

regionSelect.dispatchEvent(new Event("change"));