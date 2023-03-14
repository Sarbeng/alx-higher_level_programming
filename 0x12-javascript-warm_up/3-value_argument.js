#!/usr/bin/node
const count = process.argv.length;
const argArray = process.argv;
console.log(count === 3?  argArray[2] : 'No argument');
