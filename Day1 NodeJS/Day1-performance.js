const fs = require('fs');
// read input and split each number into an array
var Inputs = fs.readFileSync('AdventInput.txt', 'utf-8').split("\n");
// change each number into an integer
Inputs = Inputs.map(n => parseInt(n, 10));
// algorithm *-*
let our2020 = Inputs.filter(n => n + Inputs.find(k => k+n == 2020) == 2020);
console.log("Solution:", our2020[0] * our2020[1]);
