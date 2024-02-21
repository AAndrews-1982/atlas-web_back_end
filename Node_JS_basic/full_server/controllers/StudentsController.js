import { readDatabase } from '../utils.js';

export class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(process.argv[2]);
      let message = 'This is the list of our students\n';
      Object.keys(students).sort().forEach((field) => {
        message += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });
      res.status(200).send(message.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase(process.argv[2]);
      if (students[major]) {
        res.status(200).send(`List: ${students[major].join(', ')}`);
      } else {
        res.status(500).send('Cannot load the database');
      }
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
