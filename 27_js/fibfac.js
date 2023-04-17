//Team Frog Riders :: Matthew Yee, Vivian Graeber
//SoftDev pd7
//K27 -- Basic functions in JavaScript
//2023-04-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
function fact(n) {
    if (n < 2) {
        return 1;
    } else {
        return (n * fact(n - 1));
  }
}

fact(1); //"...should be  1"
fact(2); //"...should be  2"
fact(3); //"...should be  6"
fact(4); //"...should be  24"
fact(5); //"...should be  120"

function fib(n) {
    if (n <= 0) {
        return 0;
    } else if (n <= 2) {
        return 1;
    } else {
        return (fib(n - 1) + fib(n - 2));
    }
}

fib(0); //"...should be  0"
fib(1); //"...should be  1"
fib(2); //"...should be  1"
fib(3); //"...should be  2"
fib(4); //"...should be  3"

function gcd(a, b) {
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
}