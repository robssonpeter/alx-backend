import { createClient } from 'redis';

const client = createClient()
client.connect()

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value).then(resp => {
        console.log(`Reply: ${resp}`);
    });
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName).then(val => {
        console.log(val)
    });
}

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
})

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

