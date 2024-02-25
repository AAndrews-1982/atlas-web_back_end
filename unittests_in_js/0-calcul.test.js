const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('sums two rounded numbers', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('sums two rounded numbers, including a decimal rounded up', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('sums two rounded numbers, both decimals rounded up', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('sums two rounded numbers, including a decimal exactly at .5', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
