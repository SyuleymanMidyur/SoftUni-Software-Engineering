function solve(number) {
    const stringFromNum = number.toString();
    let sum = 0;
    let check = true;

    for (let i = 0; i < stringFromNum.length; i++) {
        sum += Number(stringFromNum[i])
        if (stringFromNum[i] !== stringFromNum[i+1] && i < stringFromNum.length -1)
            check = false;
    }

    console.log(check);
    console.log(sum);
    
}

solve(2222222); // true, 14