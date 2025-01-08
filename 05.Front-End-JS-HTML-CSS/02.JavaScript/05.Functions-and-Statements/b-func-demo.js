function hLine() {
    console.log('--------');
    
}

function printHeader() {
    console.log('--Header Info--');
    
}

function printMain() {
    console.log('==Print Main==');
    
}

function printDocument() {
    printHeader();
    hLine();
    printMain();
}

printDocument();


// Return Statement
function calculateSum(a, b) {
    return a + b
}

// Save returned result as varible
const result = calculateSum(3, 5);
console.log(result);

// Print returned result
console.log(calculateSum(2, 3));

// Execute method on returned result
const formatedSum = calculateSum(2, 3).toFixed(2);
console.log(formatedSum);

// Use in expression
const expressionResult = calculateSum(1,3) * 10
console.log(expressionResult);

// create function that validates array index
function isValidArrayIndex(arr, index) {
    let isValid = true;

    if (!Number.isInteger(index)) {
        isValid = false;
    }

    if (index < 0 || index >= arr.length) {
        isValid = false;
    }

    return isValid;
}

console.log(isValidArrayIndex([1,2,3,4,3,5], 2));

// Default value
function printHeader() {
    console.log('Header');
    
}

const defaultReturn = printHeader();
console.log(defaultReturn);

function printName(namesArr) {
    console.log(`${namesArr[0]} ${namesArr[1]}`);
    
}

function formatGrade(grade) {
    let result = ''
    if (grade < 3.00) {
        result = 'Fail'
        
    } else if (grade < 3.50) {
        result = 'Poor'
        
    } else if (grade < 4.50) {
        result = 'Good'        
    } else if (grade < 5.50) {
        result = 'Very good'
        
    } else if (grade >= 5.50)
        result = 'Exellent'
    
    console.log(`${result} (${grade})`);
}


// Print certificate
function printCertificates(grade, names) {
    printHeader();
    printName(names);
    formatGrade(grade);
}

printCertificates(5.95, ['Amaya', 'Midyur'])

