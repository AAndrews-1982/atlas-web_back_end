const http = require('http');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    // Adjusted indentation to comply with ESLint rules
    const lines = data.split('\n')
      .filter((line) => line)
      .slice(1);
    const students = lines.map((line) => {
      const [, , , field] = line.split(',');
      return { field };
    });

    const fields = students.reduce((acc, { field }) => {
      acc[field] = (acc[field] || 0) + 1;
      return acc;
    }, {});

    // Changed 'let' to 'const' as per ESLint recommendation
    const messageParts = [`Number of students: ${students.length}`];
    Object.entries(fields).forEach(([field, count]) => {
      // Adjusted indentation to comply with ESLint rules
      const names = lines.filter((line) => line.endsWith(field))
        .map((line) => line.split(',')[0]);
      messageParts.push(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    });

    return messageParts.join('\n');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

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
