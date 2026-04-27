// variable declaration and assignment dvhfhvhf
// const is nothing but a constant variable which cannot be re assigned and re declared.

const x = "naga";
console.log(x);
// const x="lakshmi";
// console.log(x); 

// var is variable which can be re assigned and re declared and 
// it is global scope variable we can use it anywhere in the program 

var y = "naga";
console.log(y);
var y = "lakshmi";
console.log(y);

// let is a variable which can be reassigned but cannot declared again and 
// it is block scope variable we can use it in the block only 

let z = "naga";
console.log(z);
 z = "lakshmi";
console.log(z);
 
// data types:
    //   data type  which tells use what type of data we are working with and 
    // what type of operations perform on that data.

//    here are 2 types of data types in js

//   1. primitive data types 
        //string ->    string is a sequence of characters and it is enclosed in single or double quotes
        //integer ->   it is a whole number without decimal point
        //undefined -> it is a variable which is declared but not assigned any value
        //float ->     it is a number with decimal point
       // boolean ->   it is a data type which can have only two values true or false
       // null ->      it is a data type which represents the absence of any value or object 
       

// 2. complex data types
    
    

let str = "this is a text message";
console.log(str)

let num = 34;
console.log(num)

let floatNum = 3.14;
console.log(floatNum)

let bool = 10 < 20;
let bool2 = 12>20;
console.log(bool2)
console.log(bool);

let nullValue = null;
console.log(nullValue)

let und = undefined;
console.log(und)

// complex data types
   // array ->  it is a data structure which can hold multiple values of different data types and 
                  //it is enclosed in square brackets []

let fruits=["apple", "banana", 55,{name:"naga"}];
console.log(fruits)

// object ->  it is a data structure which can hold multiple values of different data types and  
                  // it is enclosed in curly braces{}

const games = {
    game_name: "cricket",
    player : "Dhoni",
    team : "india"
}
console.log(games);

// find data type of variable by using typeof operator
// every thing in java script is an object  (imp)
console.log(typeof games);
console.log(typeof fruits);

 
// we check the particular data type by using 
console.log(Array.isArray(fruits)) ; 

// operators:
    // operators are used to perform operations on variables and values and 
    //  In programming, an operator is a symbol (like +, -, *) that represents a specific
    //  action or calculation to be performed
let b = 10;
let c = 20;
b++;
c--;


console.log(b+c);
console.log(b-c);
console.log(b*c);
console.log(b/c);
console.log(b%c);
console.log(b);
console.log(c);
 
//control flow and conditional statements
     //  control flow statements are used to control the flow of execution of the program and
    //  conditional statements are used to perform different actions based on different conditions.
     
let name= "naga";
let age = 22;
if(name === "naga" && age > 18){
    console.log("you are eligible to vote"); 

}

let first = 90
let game2 = "football";
let captain = "dhoni";

if(80<=100){
    console.log("failed")
}
else if(60<=80){
    console.log("average")

}
else{
    console.log("toppers")
    
}


// type conversion:converting one data type to another data type.

let n= "55";
let m= 10;
let o= 7.0

int_con=parseInt(n);
console.log(int_con)
console.log(typeof int_con)

str_con=String(m);
console.log(str_con)
console.log(typeof str_con)


flo_con = parseInt(o);
console.log(flo_con)
console.log(typeof flo_con)

fl_con = parseFloat(o);
console.log(fl_con)
console.log(typeof fl_con)