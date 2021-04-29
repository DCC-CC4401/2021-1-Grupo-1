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
        filters: ["Perro", "Gato", "En adopción"],
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

let page = 0;
let maxPage = 1;

let userFilters = document.getElementById("user-filters")

let withoutResults = document.getElementById("without-results")
let withResults = document.getElementById("with-results")

let nextButton = document.getElementById("next-button")
let previousButton = document.getElementById("previous-button")


for (let i = 0; i < testResults.length; i++) {
    addResult(i);
}

addFilter("Perro")
addFilter("En adopción")
updateContent()

function nextPage() {
    if (page < maxPage) {
        page += 1;
        updateContent()
    }
}

function previousPage() {
    if (page > 0) {
        page -= 1;
        updateContent()
    }
}

function updateContent() {
    if (testFilters.length > 0) {
        userFilters.style.display = "block";
    } else {
        userFilters.style.display = "none";
    }
    if (page === 0) {
        withResults.style.display = "block";
        withoutResults.style.display = "none";
    } else {
        withoutResults.style.display = "block";
        withResults.style.display = "none";
    }

    if (maxPage > page) {
        nextButton.style.display = "block";
    } else {
        nextButton.style.display = "none";
    }

    if (page > 0) {
        previousButton.style.display = "block";
    } else {
        previousButton.style.display = "none";
    }
}

function addResult(n) {
    let result = ""

    result = result + "<div class='result-item'>" +
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

function removeFilter(n) {
    let elem = document.getElementById("user-filter-" + n);
    userFilters.removeChild(elem);

    testFilters.splice(n);
}

function addFilter(text) {
    let divFilter = document.createElement("div");
    divFilter.setAttribute("class", "user-filter");
    divFilter.setAttribute("id", "user-filter-" + testFilters.length);

    let textFilter = document.createElement("div")
    textFilter.setAttribute("class", "result-filter");
    textFilter.innerHTML = text;

    let buttonFilter = document.createElement("button")
    buttonFilter.setAttribute("type", "button");
    buttonFilter.setAttribute("class", "cross-button");
    buttonFilter.setAttribute("onclick", "{removeFilter("+ testFilters.length + ");}");
    buttonFilter.innerHTML = "<img src='/static/users/media/close.svg' alt='close' class='cross-img'/>";

    divFilter.appendChild(buttonFilter);
    divFilter.appendChild(textFilter);

    userFilters.appendChild(divFilter);

    testFilters.push(text)
}