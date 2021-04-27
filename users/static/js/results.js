let page = 0;
let maxPage = 1;

let withoutResults = document.getElementById("without-results")
let withResults = document.getElementById("with-results")

let nextPageButton = document.getElementById("next-page")
let previousPageButton = document.getElementById("previous-page")

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
    if (page === 0) {
        withResults.style.display = "block";
        withoutResults.style.display = "none";
    } else {
        withoutResults.style.display = "block";
        withResults.style.display = "none";
    }

    if (maxPage > page) {
        nextPageButton.style.display = "block";
    } else {
        nextPageButton.style.display = "none";
    }

    if (page > 0) {
        previousPageButton.style.display = "block";
    } else {
        previousPageButton.style.display = "none";
    }
}