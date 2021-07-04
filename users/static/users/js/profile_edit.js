function getInitialFormSectionData(sectionSelector) {
    let initialData = {}
    getSectionInputs(sectionSelector).forEach(function (input) {
        initialData[input.id] = input.value;
    });
    return initialData;
}

function getSectionInputs(sectionSelector) {
    return document.querySelectorAll(sectionSelector + ' input, ' + sectionSelector + ' select, ' + sectionSelector + ' textarea');
}

function getSectionSubmitButton(sectionSelector) {
    return document.querySelector(sectionSelector + ' button[type=submit]')
}

function updateSubmitButton(sectionSelector, submitButton, initialData) {
    let hasChanged = false;
    let inputs = getSectionInputs(sectionSelector);
    inputs.forEach(function (input) {
        if (input.value !== initialData[input.id]) {
            // Current value is different from initial value
            hasChanged = true;
        }
    });
    submitButton.disabled = !hasChanged;
}

function addSectionEventListeners(sectionSelector) {
    let submitButton = getSectionSubmitButton(sectionSelector);
    let initialData = getInitialFormSectionData(sectionSelector);
    getSectionInputs(sectionSelector).forEach(function (input) {
        input.addEventListener('change',  () => updateSubmitButton(sectionSelector, submitButton, initialData));
        input.addEventListener('keyup',  () => updateSubmitButton(sectionSelector, submitButton, initialData));
    })
}

addSectionEventListeners('#privacy-section')
