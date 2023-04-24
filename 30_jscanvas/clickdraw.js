var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if(mode = "rect"){
        mode = "circ";
    }
    else{
        mode = "rect";
    }
}

var drawRect = function(e){
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillrect(mouseX, mouseY, 25, 100);
}

var drawCircle = (e) => {
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);

}

var draw = (e) => {
    if(mode = "rect"){
        drawRect;
    }
    else{
        drawCircle(e);
    }
}

var wipeCanvas = () => {

}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);