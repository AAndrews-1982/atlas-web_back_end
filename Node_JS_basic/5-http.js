const http = require('http');
const fs = require('fs').promises;

// Function to count students from the CSV, similar to 3-read_file_async.js
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line).slice(1); // Skip header and filter empty lines
    const students = lines.map(line => {
      const [ , , , field] = line.split(',');
      return { field };
    });

    const fields = students.reduce((acc, { field }) => {
      acc[field] = (acc[field] || 0) + 1;
      return acc;
    }, {});

    let message = `Number of students: ${students.length}\n`;
    Object.entries(fields).forEach(([field, count]) => {
      const names = lines.filter(line => line.endsWith(field)).map(line => line.split(',')[0]);
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
