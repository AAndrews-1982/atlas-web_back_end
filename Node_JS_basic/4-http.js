const http = require('http');

// Create an HTTP server
const app = http.createServer((req, res) => {
  // Set the response header to indicate plain text content
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  // Send the response body
  res.end('Hello Holberton School!');
});

// The server listens on port 1245
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Export the server
module.exports = app;
