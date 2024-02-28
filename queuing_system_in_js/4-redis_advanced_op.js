import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const hsetAsync = promisify(client.hset).bind(client);
const hgetallAsync = promisify(client.hgetall).bind(client);

function setHashValues() {
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  Object.entries(schools).forEach(([city, value], index) => {
    client.hset('HolbertonSchools', city, value, redis.print);
  });
}

async function displayHash() {
  console.log('Displaying the hash stored in Redis:');
  try {
    const hash = await hgetallAsync('HolbertonSchools');
    console.log(hash);
  } catch (err) {
    console.error(err);
  }
}

setHashValues();

// Since displayHash is async, we ensure it's called after a small delay to allow all hset operations to complete
setTimeout(() => {
  displayHash();
}, 1000);
