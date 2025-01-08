function recursiveRepeatString(string, count, n=1) {
    if (n == count) {
        return string
    };
    return string + recursiveRepeatString(string, count, n+1)
}

console.log(recursiveRepeatString('abc', 3));
console.log(recursiveRepeatString('String', 2));
