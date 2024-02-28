import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

/**
 * Simulates sending a notification.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message of the notification.
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
