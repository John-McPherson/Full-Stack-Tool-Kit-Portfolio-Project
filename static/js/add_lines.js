// adds extra recipe step and ingredient lines to the submit recipe form 

document.addEventListener('DOMContentLoaded', function () {

    buttons = document.getElementsByClassName('minus-plus');
    for (button of buttons) {
        button.addEventListener('click', incrementSteps)
    }
    addLines(stepCounter, 'step')
    addLines(ingredientCounter, 'ingredient')
})
let ingredientCounter = 5;
let stepCounter = 5;

function incrementSteps(event) {
    event.preventDefault();
    ingredientSection = document.getElementById('ingredients-section');
    if (this.id === 'ing-plus') {
        ingredientCounter++
        addLines(ingredientCounter, 'ingredient')
    } else if (this.id === 'ing-minus') {
        if (ingredientCounter !== 1) {
            ingredientCounter--
            addLines(ingredientCounter, 'ingredient')
        }

    } else if (this.id === 'step-plus') {
        stepCounter++
        addLines(stepCounter, 'step')

    } else if (this.id === 'step-minus') {
        if (stepCounter !== 1) {
            stepCounter--
            addLines(stepCounter, 'step')
        }
    }

}

function addLines(counter, type) {
    html = ``
    for (let i = 0; i < counter; i++) {
        if (type === 'step') {
            html += ` <div class="row">
            <div class="col-1 offset-1">
            <p class='input-wide  input-p align-items-center'>${i+1}.</p>
            </div>
            <div class="col-9">
            <input class='input-wide ' type="text" id="step-${i+1}" name="step" placeholder="Step">
            </div>
            </div>
            `
        } else if (type === 'ingredient') {
            html += `<div class="row">
            <div class="col-2 offset-1">
            <label for="volume-${i+1}" class='d-none'></label>
                <input class='input-wide ' type="number" name="volume" id="volume-${i+1}" placeholder="00">
            </div>
            <div class="col-2">
            <label for="measurement-${i+1}" class='d-none'></label>
                <select class='input-wide ' id="measurement-${i+1}" name="measurement">
                    <option value="ml">ml</option>
                    <option value="barspoons">bsp</option>
                    <option value="dashes">dashes</option>
                    <option value="fl-oz">fl oz</option>
                </select>
            </div>
            <div class="col-1 d-flex">
                <p class='input-wide input-p align-items-center'>of</p>
            </div>
            <div class="col-5">
            <label for="ingredient-name-${i}" class='d-none'></label>
                <input class='input-wide' type="text" id="ingredient-name-${i}" name="ingredient"
                    placeholder="ingredient">
            </div>
        </div>
    </div>`

        }
    }
    if (type === 'step') {
        document.getElementById('step-container').innerHTML = html
    } else {
        document.getElementById('ingredients-section').innerHTML = html
    }
}