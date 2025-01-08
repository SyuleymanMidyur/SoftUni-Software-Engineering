function solve(num1, num2, operator) {
    let result;
    switch (operator) {
        case '+': result = num1 + num2;
            break;
        case '-': result = num1 - num2;
            break;
        case '*': result = num1 * num2;
            break;
        case '/': result = num1 / num2;
            break;
        case '%': result = num1 % num2;
            break;
        case '**': result = num1 ** num2;
            break;
    }
    console.log(result);
    
}

solve(2, 10, '**');

// ! Don't do this at home lol

function hackySolve(num1, num2, operator) {
    let expression = `${num1} ${operator} ${num2} `;

    let result = eval(expression);
    console.log(result);
    
}

hackySolve(5, 6, '+')