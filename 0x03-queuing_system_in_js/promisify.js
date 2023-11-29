const util = require('util') 
   
// Importing File System module 
const fs = require('fs') 
   
// Use promisify to convert callback 
// based method fs.readdir to  
// promise based method 
const readdir = util.promisify(fs.readdir) 
   
const readFiles = async (path) => { 
    const files = await readdir(path) 
    console.log(files) 
  } 
   
  readFiles(process.cwd()).catch(err => { 
    console.log(err) 
  }) 