var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");
var ctx = c.getContext("2d");
ctx.fillStyle = "rgb(0, 255, 255)";
var requestID;

var clear = function(e) {
    e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear(e);
    console.log("dotting");
    window.cancelAnimationFrame(requestID);
    ctx.lineWidth = 1;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc((c.width / 2), (c.height / 2), radius, 0, (2 * Math.PI));
    ctx.fill();
    ctx.stroke();
    requestID = window.requestAnimationFrame(drawDot);
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

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 100;//scaling
    var rectHeight = 50;//also scaling
    var rectX = Math.floor(Math.random() * (c.width - rectWidth));
    var rectY = Math.floor(Math.random() * (c.height - rectHeight));
    var xVel = 1;
    var yVel = 1;
    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (((rectX + rectWidth) >= c.width) || (rectX <= 0)) {
            xVel = -xVel;
        }
        if (((rectY + rectHeight) >= c.height) || (rectY <= 0)) {
            yVel = -yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};

var stopIt = () => {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);