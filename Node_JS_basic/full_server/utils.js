import fs from 'fs/promises';

export const readDatabase = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line).slice(1);
    const students = lines.reduce((acc, line) => {
      const [name, , , field] = line.split(',');
      if (!acc[field]) acc[field] = [];
      acc[field].push(name);
      return acc;
    }, {});
    return students;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
