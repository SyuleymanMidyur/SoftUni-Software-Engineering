function formatGrade(grade) {
    let result = ''
    if (grade < 3.00) {
        result = 'Fail'
        
    } else if (3.00 <= grade < 3.50) {
        result = 'Poor'
        
    } else if (grade < 4.50) {
        result = 'Good'        
    } else if (grade < 5.50) {
        result = 'Very good'
        
    } else if (grade >= 5.50)
        result = 'Exellent'
    
    console.log(`${result} (${grade})`);
}

formatGrade(3.33)