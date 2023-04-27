// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation();
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

// Q: When user clicks on a cell, in what order will the pop-ups appear?

/*
If the boolean arg is set to true the event triggered by that event listener is higher in priority and appears before events with that arg set to false. Otherwise, pop-ups appear in the order they are listed in. stopPropagation prevents event listeners after the first one from being triggered.
*/