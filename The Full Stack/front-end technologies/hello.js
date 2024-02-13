var person;
person = "John";

console.log("Hello, " + person + "!");

var petDog = 'Rex'; // Task 1 solution
console.log(petDog);

// unstrict comparison
console.log(100 == "100");
// true

// strict comparison
console.log(100 === "100");
// flase

// block scope
let x = 10;
x = 20; // Valid - Reassigning value
console.log(x); // Output will be 20

const y = 10;
// y = 20; // Invalid - Reassigning value when using const
console.log(y); // Output will be 20