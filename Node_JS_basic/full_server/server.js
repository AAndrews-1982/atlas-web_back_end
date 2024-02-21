import express from 'express';
import router from './routes/index.js';

const app = express();
const port = 1245;

// Middleware to use for all requests, enabling JSON and URL-encoded bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Use the router from `routes/index.js`
app.use('/', router);

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

export default app;
