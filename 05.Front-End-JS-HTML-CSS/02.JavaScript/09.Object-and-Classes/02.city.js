function solve(city) {
    let cityKeys = Object.keys(city);

    for (const key of cityKeys) {
        console.log(`${key} -> ${city[key]}`);
    }
}

solve({
    name: 'Sofia',
    area: '492',
    country: 'Bulgaria',
    postCode: "1000"
})
