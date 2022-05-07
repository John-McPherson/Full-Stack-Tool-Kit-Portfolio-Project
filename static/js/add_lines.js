// adds extra recipe step and ingredient lines to the submit recipe form 

document.addEventListener('DOMContentLoaded', function () {
    buttons = document.getElementsByClassName('minus-plus');
    for (button of buttons) {
        button.addEventListener('click', incrementCounter)
    }
})
let ingredientCounter = 5;
let stepCounter = 5;
let stepPlus = false;
let ingredientPlus = false;


const extraLines = (counter, type) => {
    document.getElementsByClassName(type)[counter].classList.toggle("d-none")

}

function incrementCounter(event) {
    event.preventDefault();
    if (this.id === "step-plus") {
        if (stepPlus) {
            stepCounter++
        }
        (stepCounter > 7) ? stepCounter = 7: extraLines(stepCounter, "step")
        stepPlus = true
    } else if (this.id === "step-minus") {
        if (stepPlus == false) {
            stepCounter--
        }
        (stepCounter < 1) ? stepCounter = 1: extraLines(stepCounter, 'step')
        stepPlus = false
    } else if (this.id === "ing-plus") {
        if (ingredientPlus) {
            ingredientCounter++
        }
        (ingredientCounter > 7) ? ingredientCounter = 7: extraLines(ingredientCounter, 'ingredients')
        ingredientPlus = true
    } else if (this.id === "ing-minus") {
        if (ingredientPlus == false) {
            ingredientCounter--
        }
        (ingredientCounter < 1) ? ingredientCounter = 1: extraLines(ingredientCounter, 'ingredients')
        ingredientPlus = false
    }
}

module.exports = extraLines;