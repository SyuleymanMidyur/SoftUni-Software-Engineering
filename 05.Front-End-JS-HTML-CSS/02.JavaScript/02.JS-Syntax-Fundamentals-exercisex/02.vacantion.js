function solve(num_of_people, group, day) {
    let totalPrice;
    let dayPrice;
    if (group == 'Students') {
        switch (day) {
            case 'Friday': dayPrice = 8.45; break;
            case 'Saturday': dayPrice = 9.80; break;
            case 'Sunday': dayPrice = 10.46; break;
        }
        totalPrice = num_of_people * dayPrice

        if (num_of_people >= 30) {
            totalPrice *= 0.85
        }
    }

    if (group == 'Business') {
        switch (day) {
            case 'Friday': dayPrice = 10.90; break;
            case 'Saturday': dayPrice = 15.60; break;
            case 'Sunday': dayPrice = 16; break;
        }
        totalPrice = num_of_people * dayPrice
        
        if (num_of_people >= 100) {
            totalPrice -= 10 * dayPrice
        }
    }

    if (group == 'Regular') {
        switch (day) {
            case 'Friday': dayPrice = 15; break;
            case 'Saturday': dayPrice = 20; break;
            case 'Sunday': dayPrice = 22.50; break;
        }
        totalPrice = num_of_people * dayPrice

        if (10 <= num_of_people && num_of_people <= 20) {
            totalPrice *= 0.95
        }
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
    
}

solve(30, 'Students', 'Sunday')
solve(40, 'Regular', 'Saturday')