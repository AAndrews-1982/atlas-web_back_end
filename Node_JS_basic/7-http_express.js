const express = require('express');
const fs = require('fs').promises;

const app = express();

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line).slice(1); // Skip header and empty lines
    const students = {};
    lines.forEach((line) => { // Added parentheses around parameter
      const [name, , , field] = line.split(',');
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(name);
    });

    let message = `Number of students: ${lines.length}\n`;
    Object.keys(students).forEach((field) => { // Added parentheses around parameter
      message += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
    });

    return message.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const databasePath = process.argv[2];

app.get('/', (_req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (_req, res) => {
  try {
    const message = await countStudents(databasePath);
    res.send(`This is the list of our students\n${message}`);
  } catch (error) {
    res.send(error.message);
  }
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

module.exports = app;
