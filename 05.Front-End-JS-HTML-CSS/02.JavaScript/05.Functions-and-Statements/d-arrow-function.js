// Function to be converted to arrow function
const doubleExpression = function(number) {
    return number * 2;
}

// Arrow function with statement body
const doubleStatementBody = (number) => {
    return number * 2
}

// Arrow function with expression body
const doubleExpressionBody = (number) => number * 2;

// Arrow function with expression body with single parametar - only if it single parameter (number)
const arrowFuncSingleParametar = number => number * 2
