function solve(text, word) {
    const replacedTexed = text.replaceAll(word, '*'.repeat(word.length));
    console.log(replacedTexed);
    
}

solve('A small sentence with some words', 'small');