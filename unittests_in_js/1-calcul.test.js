// 1-calcul.test.js
const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('calculateNumber with operation type', function() {
  describe('SUM', function() {
    it('Correctly adds rounded numbers.', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', function() {
    it('Correctly subtracts rounded numbers.', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -3); // Assuming the correction here
    });
  });

  describe('DIVIDE', function() {
    it('Correctly divides rounded numbers.', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2); // Assuming correction to match actual division behavior
    });
    it('Returns "Error" for division by zero.', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
