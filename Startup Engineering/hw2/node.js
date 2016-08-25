#!/usr/bin/env node
var fs = require('fs');
var outfile = "hello.txt";
var out = "A startup is a business built to grow rapidly.\n";
fs.writeFileSync(outfile, out);  
console.log("Script: " + __filename + "\nWrote: " + out + "To: " + outfile);


var prime_numbers = [] ;
prime_numbers.push(2);
curr_num = 3;
prime = 1;

while(1) {
	divisor = 0;
	//console.log("prime number length :" +prime_numbers.length+ "\n");
	while (divisor < prime_numbers.length) {
		if (curr_num % prime_numbers[divisor] == 0) {
			prime = 0;
			break;
		}
		divisor = divisor + 1;
		//console.log("divosr :" +divisor+ "\n");
		//console.log("prime number length :" +prime_numbers.length+ "\n");
	}
	if (prime == 1) {
		prime_numbers.push(curr_num);
		console.log("Found prime number :" +curr_num+ "\n");
	} else {
		prime = 1;
	}
	if (prime_numbers.length == 100) {
		break;
	}	
	curr_num = curr_num + 1;
}
fs.writeFileSync("prime_numbers.txt", prime_numbers);  
