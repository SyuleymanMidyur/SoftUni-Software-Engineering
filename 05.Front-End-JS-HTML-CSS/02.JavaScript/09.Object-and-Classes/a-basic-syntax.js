const { log } = require("node:console");
// Object literal
let cat = {name: 'Catty', age: 1};
console.log(cat);

//Multiline literal
let town = {
    name: 'Sofia',
    population: 200000,
    country: 'Bulgaria',
};

//Empty object
let person = {};

//Set property dinamicly (runtime)
person.name = 'Amaya';
person.age = 1;
person.IsFamale = true;
console.log(person);

//Access property with dot syntax
console.log(person.name);

//Access property with bracket syntax
console.log(person['name']);

// Object literal short hand syntax
let firstName = 'Musa';
let somePerson = {
    //firstName: firstName,
    firstName, //Shorthand syntax
    age: 10,
};
console.log(somePerson);

// Declare method in literal - (property which value is a function calls method)
let robot = {
    name: 'Sony',
    clean: function() { // function expression
        console.log('robot cleaning...');
    },
    coocking: () => console.log('robot coocking...'),
    wash() {  // object method notation
        console.log('robot washing');        
    },
};

robot.clean(); // calls the method (the function)
robot.coocking();
robot.wash();

// Object values
console.log(Object.values(person));

//Object keys
console.log(Object.keys(person));

//Object entries
console.log(Object.entries(person)); // return all value key pairs in array 

// Access property by varible
let propName = 'name';
console.log(person[propName]);

// Using oligal indifier charachters
let someObj = {
    first_name: 'Pesho',
    _internalProp: 'SomeVAL',
    $special: 'special',
    'last-name': 'Peshev'
}

// Access iligal charachters in property name
console.log(someObj['last-name']);
