#!/usr/bin/node
// This is a script that reads and prints a file's content

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
