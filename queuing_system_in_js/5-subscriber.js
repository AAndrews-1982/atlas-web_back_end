import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', function() {
  console.log('Redis client connected to the server');
});

subscriber.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
