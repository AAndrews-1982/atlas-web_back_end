import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Listen for the "connect" event to log the successful connection message
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

// Listen for the "error" event to log any errors
client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
