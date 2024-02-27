const calculateNumber = require("./1-calcul.js");
const assert = require('assert');

// Describe a test suite for the updated calculateNumber function with the 'type' parameter
describe('calculateNumber', function() {
    // Testing SUM operation
    it('Correctly applies the SUM operation after rounding.', function() {
        assert.strictEqual(calculateNumber('SUM', 1.2, 3), 4); // 1.2 rounds to 1, 3 rounds to 3, 1 + 3 = 4
        assert.strictEqual(calculateNumber('SUM', 1.7, 3), 5); // 1.7 rounds to 2, 3 rounds to 3, 2 + 3 = 5
        assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5); // 1 rounds to 1, 3.7 rounds to 4, 1 + 4 = 5
        assert.strictEqual(calculateNumber('SUM', 1.5, 3.2), 5); // 1.5 rounds to 2, 3.2 rounds to 3, 2 + 3 = 5
    });

    // Testing SUBTRACT operation
    it('Correctly applies the SUBTRACT operation after rounding.', function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -3); // 1.4 rounds to 1, 4.5 rounds to 5, 1 - 5 = -4
        assert.strictEqual(calculateNumber('SUBTRACT', 4.6, 1.2), 4); // 4.6 rounds to 5, 1.2 rounds to 1, 5 - 1 = 4
    });

    // Testing DIVIDE operation
    it('Correctly applies the DIVIDE operation after rounding.', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.5); // 1.2 rounds to 1, 3.7 rounds to 4, 1 / 4 = 0.25
        assert.strictEqual(calculateNumber('DIVIDE', 9, 2.1), 4.5); // 9 rounds to 9, 2.1 rounds to 2, 9 / 2 = 4.5
    });

    // Testing DIVIDE operation with division by zero
    it('Returns "Error" for DIVIDE operation when second number rounds to zero.', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error'); // 1.4 rounds to 1, 0 rounds to 0, division by 0 = 'Error'
    });
});
