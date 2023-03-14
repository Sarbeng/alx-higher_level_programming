#!/usr/bin/node
const count = process.argv.length;
console.log(count === 3?  process.argv[2] : 'No argument');
