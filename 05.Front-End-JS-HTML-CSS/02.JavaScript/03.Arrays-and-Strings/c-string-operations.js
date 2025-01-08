// Literals
const singleQuoteLiteral = 'text';
const doubleQuoteLiteral = "text";
const templeteLiteral = `some longer ${singleQuoteLiteral}`;

// Escaping
const quoteText = 'quote: "Some Fance Quote"'; // 'quote: '\Some Fance Quote\''

// Concatenation operator
const firstString = 'Hi!'
const secondtString = 'My name is SM'
const greet = firstString + secondtString
console.log(greet);

// Concatenation method
console.log(firstString.concat(secondtString));

// Find index of substring
const text = 'The term originally referred to messages sent using the Short message Service (SMS) on mobile devices.'
const firstMassageInex = text.indexOf('message')
console.log(firstMassageInex);
const lastMassageIndex = text.lastIndexOf('message')
console.log(lastMassageIndex);

// Substring 
const subText = text.substring(0, firstMassageInex)
console.log(subText);

// Replace 
const ReplaceMassageText = text.replace('message', 'msg') // will replace only the 1st one, we can use replaceAll() to replace all in text
console.log(ReplaceMassageText);

// Split string into array
const textArray = text.split(' ')
console.log(textArray);

// Includes - check for substring
const hasMessage = text.includes('message')
console.log(hasMessage); // true 

// Repeat
console.log('Allah is the greatest '.repeat(10));

// Trim
const stringWithSpaces = '   some string  '
console.log(stringWithSpaces.trimEnd());
console.log(stringWithSpaces.trimStart());
console.log(stringWithSpaces.trim());

// Padding
let number = 10;
let binaryString = number.toString(2);
console.log(binaryString.padStart(8, '0')); // 8 = length 

let decimalNumber = 0.1;
console.log(decimalNumber.toString);
