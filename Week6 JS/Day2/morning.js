var drinksArray = ["Fanta", "Coke", "Sprite"];
console.log(drinksArray);
console.log(drinksArray[0]);
console.log(drinksArray[1]);
console.log(drinksArray[2]);

let favDrinks=["coke", "Fanta", "Tonic", "Red Bull"];
for(let i=0; i<favDrinks.length; i++){
    console.log(favDrinks[i]);
}   

let multipleOfTwo = [];

for(let i=0; i<20; i++){
    if (i%2==0){
        multipleOfTwo.push(i);
    }  
}

console.log(`Numbers between 0-20 that are multiples of 2 are:  ${multipleOfTwo}`);

const sumOfNums=(min,max)=>{
    let sum=0;
    for(let i=min; i<=max+1; i++){
        sum+=i;
    }
    return sum;
}
console.log(`Sum of all numbers from 1 to 10: ${sumOfNums(1,10)}`);

let age=15;
while(age<=18){
    console.log("You are not an adult yet");
    age++;
}
console.log("You are now an adult");

let randomNumber=0;
while(randomNumber<10){
    console.log((`Random number is: ${randomNumber}, \n Keep looking`));
    randomNumber=Math.floor(Math.random()*20);
}
console.log(`Random number found: ${randomNumber}`);

let favFilms=["The Godfather", "The Shawshank Redemption", "The Dark Knight", "The Lord of the Rings"];
favFilms.push("The Matrix");
favFilms.push("The Green Mile");
for (let i=0; i<favFilms.length; i++){
    console.log(favFilms[i]);
}