import redis from 'redis';

const publisher = redis.createClient();

publisher.on('connect', function() {
  console.log('Redis client connected to the server');
});

publisher.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
// This message won't be processed by the subscriber due to the subscriber quitting after receiving "KILL_SERVER"
publishMessage("Holberton Student #3 starts course", 400);
