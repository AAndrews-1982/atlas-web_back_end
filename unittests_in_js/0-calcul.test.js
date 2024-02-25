const calculateNumber = require("./0-calcul.js");
const assert = require('assert');

describe('calculateNumber functionality', function() {
    it('accurately sums two rounded numbers, including decimals.', function () {
        assert.strictEqual(calculateNumber(1, 3), 4, '1 + 3 should equal 4');
        assert.strictEqual(calculateNumber(1, 3.7), 5, '1 + 3.7 should round and equal 5');
        assert.strictEqual(calculateNumber(1.2, 3.7), 5, '1.2 + 3.7 should round and equal 5');
        assert.strictEqual(calculateNumber(4.6, 5.7), 11, '4.6 + 5.7 should round and equal 11');
    });

    it('correctly handles the sum of negative numbers, rounding them as expected.', function() {
        assert.strictEqual(calculateNumber(-1, -10), -11, '-1 + -10 should equal -11');
        assert.strictEqual(calculateNumber(-11.4, -38.7), -50, '-11.4 + -38.7 should round and equal -50');
    });
});
