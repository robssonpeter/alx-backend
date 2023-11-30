const kue = require('kue');
const que = kue.createQueue();

const job = que.create('push_notification_code', {
    phoneNumber: 56789876,
    message: "The first job",
  }).save(function(err) {
    if(!err){
        console.log(`Notification job created: ${job.id}`);
    }
  });
job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', (error) => {
    console.log('Notification job failed');
})
