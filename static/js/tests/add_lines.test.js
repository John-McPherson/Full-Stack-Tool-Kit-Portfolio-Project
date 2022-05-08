/**
 * @jest-environment jsdom
 */

const {
    incrementCounter,
    extraLines,
    data
} = require("../add_lines");


beforeEach(() => {
    let fs = require('fs')
    let fileContents = fs.readFileSync('templates/submit_recipe.html', "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});


describe("add lines functon", () => {
    describe("DOM tests", () => {
        test("if called with the step parameter it should add/remove the d-none class at the index it was called at", () => {
            extraLines(1, "step")
            expect(document.getElementsByClassName('step')[1].classList).toContain('d-none');
        });
        test("if called with the ingredients parameter it should add/remove the d-none class at the index it was called at", () => {
            extraLines(1, "ingredients")
            expect(document.getElementsByClassName('ingredients')[1].classList).toContain('d-none');
        });
        test("if called with the ingredients parameter if the d-none class is present it should remove it at the index it was called at", () => {
            extraLines(7, "ingredients")
            expect(document.getElementsByClassName('ingredients')[7].classList).not.toContain('d-none');
        });
        test("if called with the ingredients parameter if the d-none class is present it should remove it at the index it was called at", () => {
            extraLines(7, "step")
            expect(document.getElementsByClassName('step')[7].classList).not.toContain('d-none');
        });
    });
});

describe("increment counter function", () => {
    beforeEach(() => {
        data.stepCounter = 5;
        data.stepPlus = false;
        data.ingredientCounter = 5;
        data.ingredientPlus = false;
    });
    test("when passed the step-plus parramater if data.StepPlus is false it should not increment stepCounter", () => {
        incrementCounter('step-plus');
        expect(data.stepCounter).toBe(5);
    });
    test("when passed the step-plus parramater if data.StepPlus is true it should increment stepCounter", () => {
        data.stepPlus = true;
        incrementCounter('step-plus');
        expect(data.stepCounter).toBe(6);
    });
    test("when passed the step-plus it should set data.stepPlus to true", () => {
        incrementCounter('step-plus');
        expect(data.stepPlus).toBe(true);
    });
    test("when passed the stepPlus paramater if data.stepPlus is true it should remain true", () => {
        data.stepPlus = true;
        incrementCounter('step-plus');
        expect(data.stepPlus).toBe(true);
    });
    test("when called twice with the step-plus paramater it should increment the step counter once", () => {
        incrementCounter('step-plus');
        incrementCounter('step-plus');
        expect(data.stepCounter).toBe(6);
    });
    test("when passed the step-minus parramater if data.StepPluse is true it should not decrease stepCounter", () => {
        data.stepPlus = true;
        incrementCounter('step-minus');
        expect(data.stepCounter).toBe(5);
    });
    test("when passed the step-minus parramater if data.StepPlus is false it should decrease stepCounter", () => {
        incrementCounter('step-minus');
        expect(data.stepCounter).toBe(4);
    });
    test("when passed the step-minus it should set data.stepPlus to false", () => {
        incrementCounter('step-minus');
        expect(data.stepPlus).toBe(false);
    });
    test("when passed the step-minus paramater if data.stepPlus is false it should remain false", () => {
        data.stepPlus = false;
        incrementCounter('step-minus');
        expect(data.stepPlus).toBe(false);
    });
    test("when called twice with the step-plus paramater it should increment the step counter once", () => {
        incrementCounter('step-minus');
        incrementCounter('step-minus');
        expect(data.stepCounter).toBe(3);
    });
    test("if data.stepCounter is 8 it should reset counter to 7", () => {
        data.stepCounter = 8;
        incrementCounter('step-plus');
        expect(data.stepCounter).toBe(7);
    });
    test("if data.stepCounter is 8 it should not call extraLines function", () => {
        data.stepCounter = 8;
        incrementCounter('step-plus');
        expect(document.getElementsByClassName('step')[7].classList).toContain('d-none');
    });
    test("if data.stepCounter is 0 it should reset counter to 1", () => {
        data.stepCounter = 0;
        incrementCounter('step-minus');
        expect(data.stepCounter).toBe(1);
    });
    test("if data.stepCounter is 0 it should not call extraLines function", () => {
        data.stepCounter = 0;
        incrementCounter('step-minus');
        expect(document.getElementsByClassName('step')[0].classList).not.toContain('d-none');
    });
    test("when passed the ing-plus parramater if data.StepPlus is false it should not increment ingredientCounter", () => {
        incrementCounter('ing-plus');
        expect(data.ingredientCounter).toBe(5);
    });
    test("when passed the ing-plus parramater if data.StepPlus is true it should increment ingredientCounter", () => {
        data.ingredientPlus = true;
        incrementCounter('ing-plus');
        expect(data.ingredientCounter).toBe(6);
    });
    test("when passed the ing-plus it should set data.ingredientPlus to true", () => {
        incrementCounter('ing-plus');
        expect(data.ingredientPlus).toBe(true);
    });
    test("when passed the ingredientPlus paramater if data.ingredientPlus is true it should remain true", () => {
        data.ingredientPlus = true;
        incrementCounter('ing-plus');
        expect(data.ingredientPlus).toBe(true);
    });
    test("when called twice with the ing-plus paramater it should increment the ingredientCounter once", () => {
        incrementCounter('ing-plus');
        incrementCounter('ing-plus');
        expect(data.ingredientCounter).toBe(6);
    });
    test("when passed the ing-minus parramater if data.StepPluse is true it should not decrease ingredientCounter", () => {
        data.ingredientPlus = true;
        incrementCounter('ing-minus');
        expect(data.ingredientCounter).toBe(5);
    });
    test("when passed the ing-minus parramater if data.StepPlus is false it should decrease ingredientCounter", () => {
        incrementCounter('ing-minus');
        expect(data.ingredientCounter).toBe(4);
    });
    test("when passed the ing-minus it should set data.ingredientPlus to false", () => {
        incrementCounter('ing-minus');
        expect(data.ingredientPlus).toBe(false);
    });
    test("when passed the ing-minus paramater if data.ingredientPlus is false it should remain false", () => {
        data.ingredientPlus = false;
        incrementCounter('ing-minus');
        expect(data.ingredientPlus).toBe(false);
    });
    test("when called twice with the ing-plus paramater it should increment the ingredients counter once", () => {
        incrementCounter('ing-minus');
        incrementCounter('ing-minus');
        expect(data.ingredientCounter).toBe(3);
    });
    test("if data.ingredientCounter is 8 it should reset counter to 7", () => {
        data.ingredientCounter = 8;
        incrementCounter('ing-plus');
        expect(data.ingredientCounter).toBe(7);
    });
    test("if data.ingredientCounter is 8 it should not call extraLines function", () => {
        data.ingredientCounter = 8;
        incrementCounter('ing-plus');
        expect(document.getElementsByClassName('ingredients')[7].classList).toContain('d-none');
    });
    test("if data.ingredientCounter is 0 it should reset counter to 1", () => {
        data.ingredientCounter = 0;
        incrementCounter('ing-minus');
        expect(data.ingredientCounter).toBe(1);
    });
    test("if data.ingredientCounter is 0 it should not call extraLines function", () => {
        data.ingredientCounter = 0;
        incrementCounter('ing-minus');
        expect(document.getElementsByClassName('ingredients')[0].classList).not.toContain('d-none');
    });
});