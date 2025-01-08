function solve(text, word) {
    const pattern = new RegExp(`\\b${word}\\b`,`g`);
    const result = text.match(pattern) || []; // if undefinde or null return []
    console.log(result.length);
    
}

solve('This is a word and it also is a sentence', 'is')
