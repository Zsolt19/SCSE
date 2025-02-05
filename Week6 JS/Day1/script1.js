// function sumNum(num1, num2) {
//     console.log(num1 + num2);
// }

// sumNum(1,2);

// function sayHello(name) {
//    alert('Hello ' + name);
// }

// sayHello('Zsolt');
// function calculateTimeLeft(age) {
//     // Assuming the average lifespan is 90 years
//     const averageLifespan = 90;

//     // Calculate the remaining years
//     const yearsLeft = averageLifespan - age;

//     // Calculate the remaining months, weeks, and days
//     const monthsLeft = yearsLeft * 12;
//     const weeksLeft = yearsLeft * 52;
//     const daysLeft = yearsLeft * 365;

//     return {
//         yearsLeft: yearsLeft,
//         monthsLeft: monthsLeft,
//         weeksLeft: weeksLeft,
//         daysLeft: daysLeft
//     };
// }

// // Example usage:
// //const age = parseInt(prompt("Enter your current age: "));
// age=40;

// if (age >= 0 && age < 90) {
//     const timeLeft = calculateTimeLeft(age);
//     console.log(`You have ${timeLeft.yearsLeft} years, ${timeLeft.monthsLeft} months, ${timeLeft.weeksLeft} weeks, and ${timeLeft.daysLeft} days left until 90 years of age.`);
// } else if (age >= 90) {
//     console.log("Congratulations! You have already reached or surpassed the age of 90.");
// } else {
//     console.log("Please enter a valid age.");
// }
// function lifeRemaining(age) {
//     var yearsRemaining=90-age;
//     var days=yearsRemaining*365;
//     var weeks=yearsRemaining*52;
//     var months=yearsRemaining*12;
//     console.log("You have "+days+" days, "+weeks+" weeks, and "+months+" months left.");
//     };

// lifeRemaining(40);

// function calculateBMI(weight, height) {
//     console.log(weight / (height * height));
// }

// calculateBMI(80, 1.8); // Output: 20.061728395061728

// console.log(typeof(30.1));

// let music ='classical';
// if (music == 'classical') {
//     console.log('Oh no, not classical again!');
// }
// else if (music == 'rock') {
//     console.log('Noisy!');
// }
// else{
//     console.log('Silence is golden!');
// }

// if (true|| false) {
//     console.log('True');
// }
let age=20;

switch(age){
    case (20):
        console.log('You are 20 years old');
        break;
    case (30):
        console.log('You are 30 years old');
        break;
    default:
        console.log('You are 40 years old');
        break;
}

const grade=87;
switch(true){
    case grade>=90:
        console.log('A');
        break;
    case grade>=80:
        console.log('B');
        break;
    case grade>=70:
        console.log('C');
        break;
    case grade>=60:
        console.log('D');
        break;
    default:
        console.log('F');
        break;
}

const cars= ["Saab", "Volvo", "BMW"];
console.log(cars[1]);

let coffeeOrder= [
    "Alex - Cortado",
    "Ben - Cortado",
    "Charlie - Whatever's new"
]
coffeeOrder[2] ="Charlie - Black coffee";
console.log(coffeeOrder);
console.log(coffeeOrder.length);
coffeeOrder.push("Aaron - Latte");
console.log(coffeeOrder);
coffeeOrder.pop()
console.log(coffeeOrder);
