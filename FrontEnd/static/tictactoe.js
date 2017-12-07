let init_player = document.getElementById("player").value;
console.log("Initital player = " + init_player);

let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');


// Title image

var title_image = new Image();
title_image.src = "../static/Tic-Tac-Toe.PNG";

title_image.onload = function(){
  ctx.drawImage(title_image, 370, 30,280,200);
};

ctx.textAlign='center';

// makes gradient object, used for aesthetic appeal
let gradient=ctx.createLinearGradient(0,0,canvas.width,0);
gradient.addColorStop("0","magenta");
gradient.addColorStop("0.5","blue");
gradient.addColorStop("1.0","red");

ctx.fillStyle=gradient;


//Title
function Text(text, x, y) {
  this.text = text;
  this.x=x;
  this.y=y;
};

//var title = new Text("Tic-Tac-Toe", 500, 50);

// win counter labels
var you = new Text("You: ", 100, 300);
var bot = new Text("Bot: ",100, 350);
var tie = new Text("Tie: ", 100, 400);



function Button(text, x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    //this.clicked = false;
    //this.hovered = false;
    this.text = text;
}

function drawX(x, y){
    ctx.strokeStyle=gradient;
    ctx.beginPath();
    ctx.moveTo(x - 20, y - 20);
    ctx.lineTo(x + 20, y + 20);

    ctx.moveTo(x + 20, y - 20);
    ctx.lineTo(x - 20, y + 20);
    ctx.stroke();
}

function drawO(x, y){
  ctx.strokeStyle = 'red';
  ctx.beginPath();  
  ctx.arc(x,y,30,0,2*Math.PI);
  ctx.stroke();
}

var backButton = new Button("BACK",100, 700, 100, 50);
var restartButton = new Button("RESTART", 800, 700, 100, 50);


function drawText(txtinfo, txtcolor, txtsizefont) {
  ctx.fillStyle=txtcolor;
  ctx.font = txtsizefont;
  ctx.fillText(txtinfo.text,txtinfo.x,txtinfo.y);
}

//drawText(title, gradient, '50pt Algerian');




function drawButton(btninfo, btncol, txtcol) {
    ctx.fillStyle=btncol;
    ctx.fillRect(btninfo.x,btninfo.y,btninfo.width,btninfo.height);
    
    ctx.fillStyle=txtcol;
    ctx.font='13pt Verdana'
    ctx.fillText(btninfo.text, btninfo.x + 50, btninfo.y + 30);
}


drawButton(backButton, "yellow", "blue");
drawButton(restartButton, "yellow", "blue");

// style lines
ctx.lineCap='round';
ctx.lineWidth = 10;
ctx.strokeStyle = 'black'

// draw board
ctx.beginPath();
ctx.moveTo(290,430);
ctx.lineTo(710,430);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(290,570);
ctx.lineTo(710,570);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(430,290);
ctx.lineTo(430,710);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(570,290);
ctx.lineTo(570,710);
ctx.stroke();


// make array of the eligible moves based on x,y coordinate locations
var moves =[];
for (var j = 0; j < 3; j++){
  for(var i = 0; i < 3; i++){
    var move = {
      x: 290 + 140*i,
      y: 290 + 140*j,
      width: 140,
      height:140,
  };
  moves.push(move);
  }
}

//adjust mouse click to canvas coordinates
function getXY(canvas, event){ 
  const rect = canvas.getBoundingClientRect();
  const y = event.clientY - rect.top;
  const x = event.clientX - rect.left;
  return {x:x, y:y};
}

// determines if mouse is within a certain rect using x, y
function isInside(pos, rect) {
    return pos.x > rect.x && pos.x < rect.x+rect.width && pos.y < rect.y+rect.height && pos.y > rect.y;
}

document.addEventListener('click', function(e) {
  const XY = getXY(canvas, e);
  //use the shape data to determine if there is a collision
  
  // if back button clicked, go back to the main page
  if (isInside(getXY(canvas, e), backButton)) {
    window.location = '/';
    return;
  }
  if (isInside(getXY(canvas,e), restartButton)){
    window.location = '/tictactoe';
    return;
  }
  
  // check if a human made a move
  for (var i = 0; i < moves.length; i++){
    if (isInside(getXY(canvas,e), moves[i])){
      human_move(i);
      return;
    }
  }
  
}, false);

function human_move(move_num) {
  $.post("/human_move", {"move": move_num}, function(data) {
    console.log(data);
    render_board(data);
    if (data["bot_move"] == 1) {
      bot_move();
    }
  });
}

function bot_move() {
  $("#waiting").show();
  $.post("/bot_move", {}, function(data) {
    console.log(data);
    render_board(data);
    $("#waiting").hide();
  });
}

ctx.font = "40px Verdana";
function render_board(data) {
  //render board
  //offset values
  for (var j = 0; j < 3; j++){
    for (var i = 0; i < 3; i++){
      var val = data["" + (j * 3 + i)];
      if (val == 0) {
        // TODO this could be simplified to one function
        drawO(290 + 140*i + 75, 140 + 140*j + 215);
    }
      else if (val == 1) {
        drawX(290 + 140*i + 75, 140 + 140*j + 215);
      }
    }
  }
  // this will never execute hehehehe
  if (data["winner"] == 0){
    // TODO use text objects here (and below)
    ctx.fillStyle = 'green';
    ctx.fillText("YOU WON!", 250, 120);
  }
  if (data["winner"] == 1){
    ctx.fillStyle = 'red';
    ctx.fillText("YOU LOST!", 250, 120);
  }
  
  if (data["winner"] == -1){
    ctx.fillStyle = 'white';
    ctx.fillText("A TIE!", 250, 120);
  }
}

$(window).on("load", function() {
  // if the first player is the bot, request the bot's move
  if (init_player == 1) {
    bot_move();
  }
});