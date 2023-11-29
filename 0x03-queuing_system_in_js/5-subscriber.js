import { createClient } from "redis";
const client = createClient();
client.connect()

client.on('connect', () => {
    console.log('Redis client connected to the server');
    client.subscribe('holberton school channel');
});

client.on('message', (channel, msg) => {
    console.log(msg);
    if (msg === 'KILL_SERVER'){
        client.unsubscribe();
        client.quit();
    }
})

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
})