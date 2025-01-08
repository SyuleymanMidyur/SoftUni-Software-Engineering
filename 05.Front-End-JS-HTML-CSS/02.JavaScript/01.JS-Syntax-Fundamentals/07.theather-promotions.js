function solve(day, age) {
    let ticketPrice;
    if (0 > age || age > 122) {
        ticketPrice = 'Error!'
        
    }
    if (0 <= age && age <= 18) {
        switch (day) {
            case 'Weekday': ticketPrice = 12 + '$'; break;
            case 'Weekend': ticketPrice = 15 + '$'; break;
            case 'Holiday': ticketPrice = 5 + '$'; break;
        }
        
    }
    if (18 < age && age <= 64) {
        switch (day){
            case 'Weekday': ticketPrice = 18 + '$'; break;
            case 'Weekend': ticketPrice = 20 + '$'; break;
            case 'Holiday': ticketPrice = 12 + '$'; break;
        }
        
    }
    if (64 < age && age <= 122) {
        switch (day){
            case 'Weekday': ticketPrice = 12 + '$'; break;
            case 'Weekend': ticketPrice = 15 + '$'; break;
            case 'Holiday': ticketPrice = 10 + '$'; break;
        }
        
    }
    console.log(ticketPrice);
}

solve('Weekday', 1222)