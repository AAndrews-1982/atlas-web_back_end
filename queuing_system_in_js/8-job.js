import kue from 'kue';

/**
 * Creates push notification jobs and adds them to the provided queue.
 * @param {Object[]} jobs - Array of job objects.
 * @param {kue.Queue} queue - The Kue queue to add jobs to.
 */
function createPushNotificationsJobs(jobs, queue) {
  // Validate jobs input
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Create a job for each item in the jobs array
  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData)
      .save(err => {
        if (err) {
          console.log(`Error in job creation: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    job.on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', errorMessage => console.log(`Notification job ${job.id} failed: ${errorMessage}`))
      .on('progress', (percentage) => console.log(`Notification job ${job.id} ${percentage}% complete`));
  });
}

export default createPushNotificationsJobs;
