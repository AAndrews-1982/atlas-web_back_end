// Define a function named calculateNumber to compute the sum of two numbers
// It takes two parameters, a and b, rounds them to the nearest integer, and returns their sum

function calculateNumber(a, b) {
  // Round both parameters to the nearest integer and sum them
  return Math.round(a) + Math.round(b);
}

// Make the function available for import in other files
module.exports = calculateNumber;
