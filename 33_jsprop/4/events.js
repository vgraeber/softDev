// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

/*
The order does matter, because it is the order in which they appear, and if stopPropagation is used, event listeners attached later will not trigger. In addition, the boolean argument, if set to true, creates a separate stack which displays before events with the boolean set to false. The event with a true boolean listed last appears first.
*/