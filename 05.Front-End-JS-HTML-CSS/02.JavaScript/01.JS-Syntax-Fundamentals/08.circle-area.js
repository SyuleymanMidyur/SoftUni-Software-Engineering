function circleArea(input) {
    let result;
    let typeOfInput = typeof(input)

    if (typeOfInput === 'number') {
        result = Math.pow(input, 2) * Math.PI;
        console.log(result.toFixed(2));
        
    } else {
        result = `We can not calculate the circle area, because we receive a ${typeOfInput}.`
        console.log(result);
        
    }
}

circleArea('name')