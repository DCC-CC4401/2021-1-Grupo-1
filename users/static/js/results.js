let page = 0;
let maxPage = 1;

let withoutResults = document.getElementById("without-results")
let withResults = document.getElementById("with-results")

let nextButton = document.getElementById("next-button")
let previousButton = document.getElementById("previous-button")

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