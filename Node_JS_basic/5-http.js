const http = require('http');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line).slice(1); // Adjusted for ESLint: Added parentheses around arrow function argument, and fixed array-bracket-spacing
    const students = lines.map((line) => { // Adjusted for ESLint: Added parentheses around arrow function argument
      const [, , , field] = line.split(','); // Adjusted for ESLint: Fixed array-bracket-spacing
      return { field };
    });

    const fields = students.reduce((acc, { field }) => {
      acc[field] = (acc[field] || 0) + 1;
      return acc;
    }, {});

    let message = `Number of students: ${students.length}\n`;
    Object.entries(fields).forEach(([field, count]) => {
      const names = lines.filter((line) => line.endsWith(field)).map((line) => line.split(',')[0]); // Adjusted for ESLint: Added parentheses around arrow function argument
      message += `Number of students in ${field}: ${count}. List: ${names.join(', ')}\n`;
    });

    return message.trim();
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

// Get the database path from the command line arguments
const databasePath = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const message = await countStudents(databasePath);
      res.end(`This is the list of our students\n${message}`);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
