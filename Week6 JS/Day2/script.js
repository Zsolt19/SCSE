// let favFilms=["The Godfather", "The Shawshank Redemption", "The Dark Knight", "The Lord of the Rings"];
// favFilms.push("The Matrix");
// favFilms.push("The Green Mile");
// for (let i=0; i<favFilms.length; i++){
//     console.log(favFilms[i]);
// }
// console.log("Your 6 random numbers are:")
// for(let i =0; i<6; i++){
//     console.log(Math.ceil(Math.random()*50));
// }
// for (let i=9; i>=0; i--){
//     console.log(i);
// }
// let films=["The Godfather", "The Shawshank Redemption", "The Dark Knight", "The Lord of the Rings"];
// for (let i=0; i<films.length; i++){
//     console.log(films[i]);
// }
// function filmCheck(filmList, filmName){
//     if (filmList[2]==filmName){
//         console.log("Yay it's Ghostbusters");
//     } else {
//         console.log("Booo, we want Ghostbusters");
//     }
// }
// filmCheck(films, "Ghostbusters");
// let numContainer=[];

// for(let i=0; i<6; i++){
//     numContainer.push(Math.floor(Math.random()*30)+1);
// //    console.log(numContainer[i]);
//     if (numContainer[i]%7==0){
//         console.log(`${numContainer[i]} is divisible by seven`);
//     }
//     else {
//         console.log(`${numContainer[i]} is not divisible by seven`);
//     }
// }

var heading=document.firstElementChild.lastElementChild.firstElementChild;
heading.innerHTML="Hello World";
heading.style.color="red";
heading.style.backgroundColor="blue";

document.body.style.backgroundColor="red";