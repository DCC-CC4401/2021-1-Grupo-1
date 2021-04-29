const testResults = [
    {
        titulo: "Busco dar perro en adopción",
        descripcion: "Es un perro y lo quiero dar en adopción",
        src: "media/dog.jpeg",
        filters: ["Perro", "En adopción"],
        seen: true,
    },
    {
        titulo: "Busco regalar gato que se cree perro",
        descripcion: "Ayuda",
        src: "media/cat.jpeg",
        filters: ["Gato", "En adopción"],
        seen: false,
    },
    {
        titulo: "Mi perro busca dueño que lo entienda",
        descripcion: "No lo entiendo, no hace \"guau, guau\"",
        src: "media/hamster.jpeg",
        filters: ["Perro", "En adopción"],
        seen: true,
    }
];

let testFilters = [];

let results = 0;

let userFilters = document.getElementById("user-filters")

let withoutResults = document.getElementById("without-results")
let withResults = document.getElementById("with-results")


addFilter("Perro")
addFilter("En adopción")
addFilter("Iguana")
updateContent()


function updateContent() {
    if (testFilters.length > 0) {
        userFilters.style.display = "block";
    } else {
        userFilters.style.display = "none";
    }

    removeResults()
    results = 0;

    for (let i = 0; i < testResults.length; i++) {
        let matches = 0;
        for (let j = 0; j < testFilters.length; j++) {
            if (testResults[i].filters.includes(testFilters[j])) {
                matches += 1;
            }
        }
        if (matches === testFilters.length) {
            addResult(i);
            results += 1;
        }
    }

    if (results > 0) {
        withResults.style.display = "block";
        withoutResults.style.display = "none";
    } else {
        withoutResults.style.display = "block";
        withResults.style.display = "none";
    }

}

function removeResults() {
    while (withResults.childElementCount > 0) {
        withResults.removeChild(withResults.childNodes[0]);
    }
}

function addResult(n) {
    let result = ""

    result = result + "<div class='result-item' id='result-'" + n + ">" +
        "<img class='result-img' src='/static/users/" + testResults[n].src + " ' alt='Animal photo'>" +
        "<div class='result-body'><div class='result-header'>" + testResults[n].titulo + "</div>" +
        "<div class='result-desc'>" + testResults[n].descripcion + "</div>";

    if (testResults[n].filters.length > 0) {
        result = result + "<div class='filters'>";
    }

    for (let i = 0; i < testResults[n].filters.length; i++) {
        result = result + "<div class='result-filter'>" + testResults[n].filters[i] + "</div>";
    }

    if (testResults[n].filters.length > 0) {
        result = result + "</div>";
    }

    if (testResults[n].seen) {
        result = result + "<div class='result-eye'><img src='/static/users/media/visibility.svg' alt='Eye'></div>"
    }

    result = result + "<button type='button' class='result-button'>Ir a publicación</button></div></div>";

    withResults.innerHTML = withResults.innerHTML + result;
}

function removeFilter(text) {
    let elem = document.getElementById("user-filter-" + text);
    userFilters.removeChild(elem);

    testFilters.splice(testFilters.indexOf(text), 1);
    updateContent();
}

function addFilter(text) {
    if (testFilters.includes(text)) {
        return;
    }

    let divFilter = document.createElement("div");
    divFilter.setAttribute("class", "user-filter");
    divFilter.setAttribute("id", "user-filter-" + text);

    let textFilter = document.createElement("div")
    textFilter.setAttribute("class", "result-filter");
    textFilter.innerHTML = text;

    let buttonFilter = document.createElement("button")
    buttonFilter.setAttribute("type", "button");
    buttonFilter.setAttribute("class", "cross-button");
    buttonFilter.innerHTML = "<img src='/static/users/media/close.svg' alt='close' class='cross-img'/>";
    buttonFilter.onclick = function () {removeFilter(text);}

    divFilter.appendChild(buttonFilter);
    divFilter.appendChild(textFilter);

    userFilters.appendChild(divFilter);

    testFilters.push(text)
}