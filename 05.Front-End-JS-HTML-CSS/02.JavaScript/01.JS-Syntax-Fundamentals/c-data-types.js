// Numbers
let intigerNumber = 10;
let decimalNumber = 3.14;
let negativeNumber = -10;
let maxPreciseNumber = Number.MAX_SAFE_INTEGER;
let maxDoublePreciseNumber = Number.MAX_VALUE;
let notANumber = NaN;
let infinity = Infinity;

// String
let singleQuoteLiteral = 'Syuleyman';
let doubleQuoteLiteral = "Amaya";
let templateLiteral = `Amaya`;

// Undefined
let undf = undefined;

// Null
let empty = null;

// BigInt
let bigNumber = BigInt(76576)
let bigNumber2 = 76576n;

// Using const
const lastName = 'Midyur' //promenliva koqto ne moje da se promenq poveche

// Block scope - ne moje da se dostypva otvyn osven ako ne sme definirali s 'var'
{
    someVarible = 'varible'
}

// Cast string to number
let someNumber = parseInt('10');
let someNumber2 = parseFloat('12.5');
let parseNumber = Number('3.14');

//NaN example
console.log(Number('Amaya'));