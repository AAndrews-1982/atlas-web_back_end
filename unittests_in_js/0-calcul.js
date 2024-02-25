function calculateNumber(a, b) {
    // Directly return the sum of rounded numbers if both are numbers
    if (typeof a === 'number' && typeof b === 'number') {
        return Math.round(a) + Math.round(b);
    } else {
        // If either a or b is not a number, handle the error or invalid input explicitly
        console.error("Invalid input: both a and b must be numbers.");
        return null; // Return null to indicate the error situation
    }
}

module.exports = calculateNumber;
