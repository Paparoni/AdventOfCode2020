const fs = require('fs');

// read input and split each number into an array
var Inputs = fs.readFileSync('AdventInput.txt', 'utf-8').split("\n");
// change each number into an integer
for(let i = 0; i <Inputs.length; i++){
    Inputs[i] = parseInt(Inputs[i]);
}
// nested for loop bam bam skip diddly doo
var get2020 = function(){
    for(let i = 0; i < Inputs.length; i++){
        for(let x = 0; x < Inputs.length; x++){
            if(Inputs[i] + Inputs[x] == 2020){
                var table = {
                    a: Inputs[i],
                    b: Inputs[x]
                }
                return table
            }
        }
    }
}

var our2020 = get2020();

// multiply our 2 numbers
var solution = our2020.a * our2020.b;

console.log("Solution:", solution);