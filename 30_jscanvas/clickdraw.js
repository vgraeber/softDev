var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect"){
        mode = "circ";
    } else {
        mode = "rect";
    }
}

var drawRect = function(e){
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "rgb(255, 0, 0)";
    ctx.lineWidth = 1;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.rect(mouseX, mouseY, 25, 100);
    ctx.fill();
    ctx.stroke();
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "rgb(255, 0, 0)";
    ctx.lineWidth = 1;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.ellipse(mouseX, mouseY, 25, 25, 0, 0, (2 * Math.PI));
    ctx.fill();
    ctx.stroke();
}

var draw = (e) => {
    if (mode == "rect") {
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);