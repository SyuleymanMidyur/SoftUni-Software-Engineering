// Array literal
let names = ['SM', 'AM', 'NM'];

// Declare an empty arrray
let emptyArray = [];

// Dynamic length
console.log(emptyArray.length);
console.log(emptyArray);
emptyArray.length = 10
console.log(emptyArray.length);
console.log(emptyArray);


//Mixed array -> not a good practice
let mixed = ['sm', 30, true,]
console.log(mixed);

// Dense array vs Sparse
let denseArr = [undefined, undefined, undefined];
let sparseArr = [];
sparseArr.length = 3;

console.log(denseArr.length === sparseArr.length); // true
console.log(denseArr); // take a space in the memort
console.log(sparseArr); // not taking space in memory 

// Number array
let numbers = [10, 20, 30, 40];

// Access elements (by index)
console.log(names[0]); // get first element
console.log(names[names.length -1]); // get last element

// Access non existant element
console.log(names[30]); // undefined

// Set element
names[0] = 'mc' // update element
names[3] = 'ss' // add element

// Array destructuring assignment
let [firstName, secondName, thirdName, fourthName] = names;
console.log(firstName);
console.log(secondName);
console.log(thirdName);
console.log(names); // Original array is untouched

// Partial destructuring
const [fName, sName] = names;

// Take the rest of the elements with partrial destructuring using rest operator
const [first, second, ...restNames] = names;
console.log(first);
console.log(second);
console.log(restNames);

// iterate array
for (let i = 0; i < names.length; i++) {
    console.log(names[i]);
    
}

// Iterate array with FOR-OF
for (let name of names) {
    console.log(name);
}

// Print array nums
function solve(numbers) {
    let output = '';

    for (const number of numbers) {
        output += `${number} `;
    }
    console.log(output.trim()); // trim premahva intervalite ot lqvo i ot dqsno
}

