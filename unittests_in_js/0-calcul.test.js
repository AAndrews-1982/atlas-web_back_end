// Import the calculateNumber function from the 0-calcul.js module
const calculateNumber = require("./0-calcul.js")
// Import the assert module for performing assertions
const assert = require('assert');

// Describe a test suite for the calculateNumber function
describe('calculateNumber', function() {
    // Test case: Checks if the function correctly rounds the first number and returns the sum
    it('Correctly rounds the first number and returns the sum.', function () {
        assert.equal(calculateNumber(1.2, 3), 4); // First number rounded
        assert.equal(calculateNumber(1.7, 3), 5); // First number rounded up
    });

    // Test case: Checks if the function correctly rounds the second number and returns the sum
    it('Correctly rounds the second number and returns the sum.', function () {
        assert.equal(calculateNumber(1, 3.2), 4); // Second number rounded
        assert.equal(calculateNumber(1, 3.7), 5); // Second number rounded up
    });

    // Test case: Checks if the function correctly rounds both numbers and returns the sum
    it('Correctly rounds both numbers and returns the sum.', function () {
        assert.equal(calculateNumber(1.2, 3.7), 5); // Both numbers rounded
        assert.equal(calculateNumber(4.6, 5.7), 11); // Both numbers rounded up
    });

    // Test case: Verifies the function works as expected with negative numbers
    it('Correctly handles rounding of negative numbers and returns the sum.', () => {
        assert.strictEqual(calculateNumber(-1.2, -10.8), -12); // Negative numbers rounded
        assert.strictEqual(calculateNumber(-11.4, -38.7), -50); // Negative numbers rounded
    });
});
