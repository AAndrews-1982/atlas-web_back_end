const express = require('express');

const app = express();

app.get('/', (_req, res) => { // Use _req to indicate an unused parameter, following some linting conventions
  res.send('Hello Holberton School!');
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

module.exports = app;
