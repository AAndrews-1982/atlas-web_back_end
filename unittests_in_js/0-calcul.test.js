const calculateNumber = require("./0-calcul.js");
const assert = require('assert');

describe('Testing calculateNumber functionality', function() {
    it('accurately calculates the sum of two rounded numbers, handling decimals correctly.', function () {
        assert.strictEqual(calculateNumber(1, 3), 4, 'Rounding 1 and 3 should yield 4');
        assert.strictEqual(calculateNumber(1, 3.7), 5, 'Rounding 1 and 3.7 should yield 5');
        assert.strictEqual(calculateNumber(1.2, 3.7), 5, 'Rounding 1.2 and 3.7 should yield 5');
        assert.strictEqual(calculateNumber(4.6, 5.7), 11, 'Rounding 4.6 and 5.7 should yield 11');
    });

    it('correctly sums up rounded negative numbers, demonstrating rounding logic with negatives.', function() {
        assert.strictEqual(calculateNumber(-1, -10), -11, 'Rounding -1 and -10 should yield -11');
        assert.strictEqual(calculateNumber(-11.4, -38.7), -50, 'Rounding -11.4 and -38.7 should yield -50');
    });
});
