const text = 'Velit exercitation aliquip Amet id reprehenderit ad duis nulla et Labore excepteur nisi culpa.'
// Regular Expressions literal
const pattern = /[A-Z][a-z]+/g;

// RegEx class
const pattern2 = new RegExp('[A-Z][a-z]+', 'g');

// REGEX METHODS
// Test method
const result = pattern.test(text);
console.log(result); // return true or false

// Exec method 
const exectResult = pattern.exec(text);
console.log(exectResult);

// Match
const matchResult = text.match(pattern);
console.log(matchResult); // return all matched without index, if we use global in the pattern returns the 1st with index

// Match All
console.log('Match All -----');

const matchAllResult = text.matchAll(pattern);
for (const match of matchAllResult) {
    console.log(match);
    
}

// Replace
let replaceText = text.replace(pattern, '*****');
console.log(replaceText);

// Split
let input = 'first.second/third|forth';
const words = input.split(/[\.\/|]/g);
console.log(words);
