function calculateNumber(a, b) {
    // Check if both arguments are of type number
    if (typeof a !== 'number' || typeof b !== 'number') {
        // Explicitly return null for invalid inputs
        return null;
    }
    // Round the numbers and return their sum
    return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
