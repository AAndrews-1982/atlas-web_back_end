import redis from 'redis';
const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

/**
 * Sets the value for the key `schoolName` in Redis.
 * @param {string} schoolName The key under which to store the value.
 * @param {string} value The value to store.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Logs the value for the given key `schoolName` from Redis.
 * @param {string} schoolName The key whose value to retrieve.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) throw err;
    console.log(reply);
  });
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
