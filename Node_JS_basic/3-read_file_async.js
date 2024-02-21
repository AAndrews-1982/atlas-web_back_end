const fs = require('fs').promises;

async function countStudents(path) {
  return new Promise(async (resolve, reject) => {
    try {
      // Asynchronously read the file content
      const data = await fs.readFile(path, 'utf8');

      // Split the file content by new line and filter out any empty lines
      const lines = data.split('\n').filter(line => line !== '');

      // Remove the header row
      lines.shift();

      // Initialize a map to hold counts of students in each field
      const fieldCounts = {};

      lines.forEach((line) => {
        const student = line.split(',');
        const field = student[3]; // Assuming the field is in the fourth column

        if (!fieldCounts[field]) {
          fieldCounts[field] = [];
        }

        fieldCounts[field].push(student[0]); // Assuming the first name is in the first column
      });

      const message = [`Number of students: ${lines.length}`];

      Object.keys(fieldCounts).forEach((field) => {
        message.push(`Number of students in ${field}: ${fieldCounts[field].length}. List: ${fieldCounts[field].join(', ')}`);
      });

      console.log(message.join('\n'));
      resolve(message.join('\n'));
    } catch (error) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = countStudents;
