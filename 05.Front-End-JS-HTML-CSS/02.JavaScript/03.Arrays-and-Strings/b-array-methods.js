let cars = ['Mercedes', 'BMW', 'Audi', 'Volkswagen']

// Pop - remove last element (mutanting)
let lastCar = cars.pop(); // will take the last element but also remove it from the array
console.log(cars);

// Push - add element at the end (mutanting)
cars.push('Audi')

// Push multiple elements
cars.push('Bently', 'Rolls Roys')
console.log(cars);

// Shift - remove first element (mutanting)
cars.shift();
console.log(cars);

// Unshift - add element in the begining of the array (mutanting)
cars.unshift('Mercedes')
console.log(cars);

// Splice - remove element at position (mutanting)
let removedCars = cars.splice(2, 1) // 2 position, 1 how many elements wants to remove | return array
console.log(cars);

// Splice - add element at specific position
cars.splice(2, 0, 'Lambo') // 2 position, 0 element to delet and after that what you want to add
console.log(cars);

// Reverse elements (mutanting)
cars.reverse();
console.log(cars);

// Join array into a string (not mutanting)
let result = cars.join(', ')
console.log(result);

// Slice takes sub array (non mutanting)
let middleCars = cars.slice(2, 4); // inclusive first interval but not the 2nd one
console.log(middleCars);
console.log(cars);
let endCars = cars.slice(4); // it will take the elements till the end if no 2nd interval
let coppyCars = cars.slice(); // if no intervals will take the whole array

// Reverse without mutanting
let reversedCarss = cars.slice().reverse();
console.log(reversedCarss);

// Includes - check if element is in the array
const hasBMW = cars.includes('BMW');
console.log(hasBMW);

// Includes - check if element is in the array after spec inxex
console.log(cars.includes('Lambo', 4));

// IndexOf - find index of element, if we are looking for element its not existing return -1,
const audiIndex = cars.indexOf('Audi');
console.log(audiIndex);


// forEach - execute code for every element (non mutanting) interative
function printElement(element) {
    console.log(element);
    
}
cars.forEach(printElement)

cars.forEach(element => {
    console.log(element.toUpperCase());
    
});

// Map create a new array with values based on original values (non mutanting)
const lowerCaseCars = cars.map(function(car) {
    return car.toLowerCase();
});
console.log(lowerCaseCars);

// Find - find the element (non mutanting) (iterativen)
let carWithL = cars.find(function(car) {
    return car.startsWith('L');
});
console.log(carWithL);

// Filter - find all elements based on condition (non mutanting) (interative)
const carsWithB = cars.filter(function(car) {
    return car.startsWith('B');
});
console.log(carsWithB);
