var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var ctx = c.getContext("2d");
ctx.fillStyle = "rgb(0, 255, 255)";
var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear();
    ctx.lineWidth = 1;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc((c.width / 2), (c.height / 2), radius, 0, (2 * Math.PI));
    ctx.fill();
    ctx.stroke();
    requestID = window.requestAnimationFrame(drawDot);
    window.cancelAnimationFrame(requestID - 1);
    if (radius == (c.width / 2)) {
        growing = false;
    }
    if (radius == 0) {
        growing = true;
    }
    if (growing) {
        radius += 1;
    } else {
        radius -= 1;
    }
};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    if (requestID != null) {
        window.cancelAnimationFrame(requestID);
    }
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);