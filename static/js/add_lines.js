// adds extra recipe step and ingredient lines to the submit recipe form 

buttons = document.getElementsByClassName('minus-plus');
for (button of buttons) {
    button.addEventListener('click', incrementSteps)
}
ingredientCounter = 1;
stepCounter = 1;

function incrementSteps(event) {
    event.preventDefault();
    ingredientSection = document.getElementById('ingredients-section');
    if (this.id === 'ing-plus') {
        ingredientCounter++
    } else if (this.id === 'ing-minus') {
        if (ingredientCounter !== 1) {
            ingredientCounter--
        }

    } else if (this.id === 'step-plus') {
        stepCounter++

    } else if (this.id === 'step-minus') {
        if (stepCounter !== 1) {
            stepCounter--
        }
    }
}