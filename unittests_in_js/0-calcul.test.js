// Import the calculateNumber function from the 0-calcul.js module
const calculateNumber = require("./0-calcul.js")
// Import the assert module for performing assertions
const assert = require('assert');

// Describe a test suite for the calculateNumber function
describe('calculateNumber', function() {
    // Test case: Checks if the function correctly returns the sum of two rounded numbers
    it('Returns the sum of two rounded numbers.', function () {
        // Assert that calculateNumber correctly sums and rounds the input numbers
        assert.equal(calculateNumber(1, 3), 4);
        assert.equal(calculateNumber(1, 3.7), 5);
        assert.equal(calculateNumber(1.2, 3.7), 5);
        assert.equal(calculateNumber(4.6, 5.7), 11);
    });

    // Test case: Verifies the function works as expected with negative numbers
    it('Returns the sum of two negative rounded numbers.', () => {
        // Perform strict equality checks to ensure accurate rounding and summing of negative numbers
        assert.strictEqual(calculateNumber(-1, -10), -11);
        assert.strictEqual(calculateNumber(-11.4, -38.7), -50);
    });
});
