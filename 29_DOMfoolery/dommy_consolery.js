//Team Frog Riders :: Matthew Yee, Vivian Graeber
//SoftDev pd7
//K27 -- Basic functions in JavaScript
//2023-04-17
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


//adds an item to the list
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


//removes an item from the list
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


//adds the 'red' class to all items in the list that do not already have it
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


//adds the 'red' and 'blue' classes to each item in the list in alternating order
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
var fib = function(n) {
  if (n <= 0) {
      return 0;
  } else if (n <= 2) {
      return 1;
  } else {
      return (fib(n - 1) + fib(n - 2));
  }
};


// FAC
var fact = function(n) {
  if (n < 2) {
      return 1;
  } else {
      return (n * fact(n - 1));
}
};


// GCD
const gcd = (a, b) => {
  let l;
  let s;
  if (a > b) {
      l = a;
      s = b;
  } else if (b > a) {
      l = a;
      s = b;
  } else {
      return a;
  }
  for (let i = s; i >= 1; i--) {
      if (((l % i) == 0) && ((s % i) == 0)) {
          return i;
      }
  }
};

var fibbutton = document.getElementById("fib");
var facbutton = document.getElementById("fac");
var gcdbutton = document.getElementById("gcd");

fibbutton.addEventListener('click', ()=>{addItem('fib(4) = ' + fib(4))});
facbutton.addEventListener('click', ()=>{addItem('fact(4) = ' + fact(4))});
gcdbutton.addEventListener('click', ()=>{addItem('gcd(12,18) = ' + gcd(12,18))});

stripe();

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

