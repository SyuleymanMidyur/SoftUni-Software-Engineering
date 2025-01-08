// Function declaration
function printText(text) {
    console.log(text);
    
}

// Function invokation (calling the function)
printText('Hello functions');

// Function hoistig
printSumResult(10, 20); // this can be called before initialization

function printSumResult(first, second) {
    console.log(first + second);
    
}

// Function expression
const subtractNumbers = function (a, b) {
    console.log(a - b);
    
};
