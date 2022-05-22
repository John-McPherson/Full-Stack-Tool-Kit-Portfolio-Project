// adds extra recipe step and ingredient lines to the submit recipe form 

document.addEventListener('DOMContentLoaded', function () {
    let buttons = document.getElementsByClassName('minus-plus');
    for (let button of buttons) {
        button.addEventListener('click', addLines);
    }
});

const data = {
    'ingredientCounter': 5,
    'stepCounter': 5,
    'stepPlus': false,
    'ingredientPlus': false
};


function addLines(event) {
    event.preventDefault();
    incrementCounter(this.id);
}

const extraLines = (counter, type) => {
    document.getElementsByClassName(type)[counter].classList.toggle("d-none");

};

function incrementCounter(id) {
    /* jshint expr: true */
    if (id === "step-plus") {
        if (data.stepPlus) {
            data.stepCounter++;
        }
        (data.stepCounter > 7) ? data.stepCounter = 7: extraLines(data.stepCounter, "step");
        data.stepPlus = true;
    } else if (id === "step-minus") {
        if (data.stepPlus == false) {
            data.stepCounter--;
        }
        (data.stepCounter < 1) ? data.stepCounter = 1: extraLines(data.stepCounter, 'step');
        data.stepPlus = false;
    } else if (id === "ing-plus") {
        if (data.ingredientPlus) {
            data.ingredientCounter++;
        }
        (data.ingredientCounter > 7) ? data.ingredientCounter = 7: extraLines(data.ingredientCounter, 'ingredients');
        data.ingredientPlus = true;
    } else if (id === "ing-minus") {
        if (data.ingredientPlus == false) {
            data.ingredientCounter--;
        }
        (data.ingredientCounter < 1) ? data.ingredientCounter = 1: extraLines(data.ingredientCounter, 'ingredients');
        data.ingredientPlus = false;
    }

}

module.exports = {
    extraLines,
    incrementCounter,
    data

};