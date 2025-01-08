// Aritmetic operators
console.log(5 + 10); // additional operator, result: 15
console.log(5 + '10'); // conocatenation operator, result: 510
console.log(1 + 2 + '3'); // 33

// division
console.log(9 / 2); // 4.5

// module
console.log(9 % 2); // 1

// exponentiation

console.log(10 ** 2); // 10 na stepen 2

// Comparison operators
let a = 5
let b = '5'
console.log(a == b); // equality operator, result: true, enabled coercion
console.log(a === b); // identity operator, result:false, equality without enabled coercion

console.log(a != b); // false
console.log(a !== b); // true

// ternary operator
console.log(a == b ? 'Equal with coercion' : 'Not equal');

// logical operators
console.log(!true); // not operator, result: false
console.log(!!true); // not-not operator, result: true

// AND logical operator -> &&

// Or logical operator -> || 

// Not operator -> !

// Rule! Comparison operators have greater priority than logical operators

// Typeof operator

console.log(typeof 5);
console.log(typeof 'Amaya');
console.log(typeof true);
console.log(typeof 100000n);
console.log(typeof undefined);
console.log(typeof Symbol('amaya'));
console.log(typeof null);

// Truthy
console.log(Boolean([]));
console.log(Boolean({}));

// Falsy values
console.log(Boolean(0)); // all other nums are truthy
console.log(Boolean(NaN));
console.log(Boolean('')); // only empty string is falsy
console.log(Boolean(null));
console.log(Boolean(undefined));