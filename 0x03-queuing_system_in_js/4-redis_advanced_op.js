import { createClient } from 'redis';

const client = createClient();
client.connect()

client.on('connect', () => {
    console.log('connected');
    client.hSet('HolbertonSchools', 'portland', 50).then((resp) => {
        console.log(`Reply: ${resp}`);
    })
    client.hSet('HolbertonSchools', 'Seattle', 80).then((resp) => {
        console.log(`Reply: ${resp}`);
    })
    client.hSet('HolbertonSchools', 'New York', 20).then((resp) => {
        console.log(`Reply: ${resp}`);
    })
    client.hSet('HolbertonSchools', 'Bogota', 20).then((resp) => {
        console.log(`Reply: ${resp}`);
    })
    client.hSet('HolbertonSchools', 'Cali', 40).then((resp) => {
        console.log(`Reply: ${resp}`);
    })
    client.hSet('HolbertonSchools', 'Paris', 2).then((resp) => {
        console.log(`Reply: ${resp}`);
    })

    client.hGetAll('HolbertonSchools').then((resp) => {
        console.log(resp)
    });
})