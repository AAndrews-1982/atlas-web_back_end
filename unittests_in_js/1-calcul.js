// Define a function named calculateNumber to compute based on the operation type
// It takes three parameters: type (string), a, and b
// Rounds a and b to the nearest integer before performing the operation

function calculateNumber(type, a, b) {
  // Round both parameters to the nearest integer
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  // Perform operation based on type
  switch (type) {
    case 'SUM':
      return roundedA + roundedB;
    case 'SUBTRACT':
      return roundedA - roundedB;
    case 'DIVIDE':
      if (roundedB === 0) {
        return 'Error'; // Return 'Error' if b rounds to 0 to avoid division by zero
      }
      return roundedA / roundedB;
    default:
      throw new Error('Invalid type'); // Handle invalid type
  }
}

// Make the function available for import in other files
module.exports = calculateNumber;
