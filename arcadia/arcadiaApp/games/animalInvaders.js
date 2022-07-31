console.log("Welcome to Animal Invaders!")

const BULLETFREQ = 10
const ANIMALFREQ = 30


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

var animalWidth = 70
var animalHeight = 70

var playerX = canvas.width/2 //topLEFT 
var playerY = canvas.height-playerHeight

var playerWidth = 100

var gameWon = false

var bullets = []

var animals = [];

var images = []


//Images thanks to Kenney.nl!
elephant = new Image();
elephant.src = 'ast/icons/elephant.png';
images.push(elephant)

giraffe = new Image();
giraffe.src = 'ast/icons/giraffe.png';
images.push(giraffe)

hippo = new Image();
hippo.src = 'ast/icons/hippo.png';
images.push(hippo)

monkey = new Image();
monkey.src = 'ast/icons/monkey.png';
images.push(monkey)

panda = new Image();
panda.src = 'ast/icons/panda.png';
images.push(panda)

parrot = new Image();
parrot.src = 'ast/icons/parrot.png';
images.push(parrot)

penguin = new Image();
penguin.src = 'ast/icons/penguin.png';
images.push(penguin)

pig = new Image();
pig.src = 'ast/icons/pig.png';
images.push(pig)

rabbit = new Image();
rabbit.src = 'ast/icons/rabbit.png';
images.push(rabbit)

snake = new Image();
snake.src = 'ast/icons/snake.png';
images.push(snake)


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
    let toDelete = [];
    for (var bullet of bullets) {
        for (i = 0; i< animals.length;++i) {
            let animal = animals[i];
            if (!(bullet["X"] > animal["X"] + animalWidth || bullet["X"] + bulletWidth < animal["X"] || bullet["Y"] + bulletHeight < animal["Y"] || bullet["Y"] > animalHeight + animal["Y"] ) ) {
                if (toDelete[toDelete.length-1] != i)
                    toDelete.push(i);
            }
        }
    
    }
    console.log(toDelete)

    var deleted = 0;
    for (var index of toDelete) {
        animals.splice(index-deleted,1);
        deleted = deleted+1;
        score += 1;
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

function randomChoose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
  }

function animateAnimals() {
    animals = animals.map((animal) => {return {"X":animal["X"]+5,"Y":animal["Y"],"image":animal["image"]}}).filter(animal => (animal.X < canvasW)); //Move and kill off-screen animals

    if (frameID % ANIMALFREQ == 0) {
        thisTime = randomChoose(images)
        animals.push({"X":10,"Y":25,"image":thisTime}) 
    }
    for (var animal of animals) {
        newImage = animal["image"]
        ctx.beginPath();
        ctx.drawImage(newImage, 0, 0,newImage.width,newImage.height,animal["X"],animal["Y"],animalWidth,animalHeight);
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
    animateAnimals()

    requestAnimationFrame(draw);

    //if (gameWon == false) {
    //    setTimeout(draw,1000)
   // }
}
draw()

