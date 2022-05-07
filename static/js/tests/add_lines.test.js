/**
 * @jest-environment jsdom
 */
const incrementCounter = require("../add_lines");
const extraLines = require("../add_lines");

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

// describe("add lines", () => {
//     describe("increment counter function", () => {
//         test('if counter is 4 should return 5', () => {
//             expect(incrementCounter(event)).toBe(5);
//         })

//     });
// });