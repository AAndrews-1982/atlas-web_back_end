import redis from 'redis';
import { promisify } from 'util';
const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

// Keep the setNewSchool function as is
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Modify the displaySchoolValue function to use async/await
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

// Test the functions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
