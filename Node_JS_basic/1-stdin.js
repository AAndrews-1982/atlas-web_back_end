// Import the readline module to handle command line input/output
const readline = require('readline');

// Create an interface for input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Display the welcome message and prompt for the user's name
console.log('Welcome to Holberton School, what is your name?');

// Event listener for receiving input
rl.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  // Once the input is received and displayed, close the readline interface
  rl.close();
});

// Event listener for close event
rl.on('close', () => {
  console.log('This important software is now closing');
});
