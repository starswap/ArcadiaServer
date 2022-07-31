console.log("Welcome to Animal Invaders!")

const BULLETFREQ = 10

var navheight = 80

var canvas = document.getElementById("gamecanvas");
canvas.width = document.body.clientWidth; //document.width is obsolete
canvas.height = document.body.clientHeight-navheight; //document.height is obsolete
var canvasW = canvas.width;
var canvasH = canvas.height;

var frameID = 0
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#1C491F";
ctx.strokeStyle = "#1C491F";

var score = 0

var playerHeight = 20
var bulletWidth = 10
var bulletHeight = 10

var playerX = canvas.width/2 //topLEFT 
var playerY = canvas.height-playerHeight

var playerWidth = 100

var gameWon = false

var bullets = []



document.addEventListener("keydown", keyDownHandler, false);

function keyDownHandler(e) {
    if(e.code  == "ArrowRight") {
        console.log(playerX)
        playerX += 5
        playerX = Math.min(playerX,canvasW-playerWidth)
    }
}

function animateBullets() {
    bullets = bullets.map((bullet) => {return {"X":bullet["X"],"Y":bullet["Y"]-2}}).filter(bullet => (bullet.Y > 0)); //Move and kill off-screen bullets
    if (frameID % BULLETFREQ == 0) {
        bullets.push({"X":playerX+playerWidth/2-bulletWidth/2,"Y":playerY-10})
    }
    for (var bullet of bullets) {
        ctx.beginPath();
        ctx.rect(bullet["X"], bullet["Y"], bulletWidth, bulletHeight);
        ctx.fill();
        ctx.stroke();
    }    
    
    //console.log(bullets)
    //ctx.end
}


var prevFact = 0


var hammertime = new Hammer(canvas);
hammertime.on('pan', function(ev) {
    playerX -= prevFact
	playerX += ev.deltaX
    prevFact = ev.deltaX
    playerX = Math.min(playerX,canvasW-playerWidth)    
    playerX = Math.max(playerX,0)    
});



function drawScore() {
    ctx.font = "16px Arial";
    ctx.fillText("Score: "+ score, 0, 20);
}


function draw() {
    frameID++;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawScore();
    
    ctx.beginPath();
    ctx.rect(playerX, playerY, playerWidth, playerHeight);
    ctx.rect(playerX+playerWidth/2-bulletWidth/2, playerY-20, bulletWidth, bulletHeight);
    ctx.rect(playerX+playerWidth/2-bulletWidth*1.5, playerY-10, bulletWidth*3, bulletHeight);
    
    ctx.fill();

    ctx.stroke()
    animateBullets()
    requestAnimationFrame(draw);

    //if (gameWon == false) {
    //    setTimeout(draw,1000)
   // }
}
draw()

