//this might be how we need to do things
//https://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit

// set up HTML5 canvas
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

ctx.textAlign='center';

let gradient=ctx.createLinearGradient(0,0,canvas.width,0);
gradient.addColorStop("0","magenta");
gradient.addColorStop("0.5","blue");
gradient.addColorStop("1.0","red");

ctx.fillStyle=gradient;


// Title, subtitle and prompt for homepage
function Text(text, x, y) {
  this.text = text;
  this.x=x;
  this.y=y;
};

//var title = new Text("*Botter Than You*", 500, 55);
var subtitle = new Text("Get ready to lose",500, 130);
//var prompt = new Text("Select Your Poison", 500,200);

function Button(text, x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    //this.clicked = false;
    //this.hovered = false;
    this.text = text;
};


function drawText(txtinfo, txtcolor, txtsizefont) {
  ctx.strokeStyle=txtcolor;
  ctx.font = txtsizefont;
  ctx.strokeText(txtinfo.text,txtinfo.x,txtinfo.y);
  
}

//drawText(title, gradient, '50pt Algerian');
drawText(subtitle, gradient,'30pt Helvetica');
//drawText(prompt, gradient, '40pt Helvetica');

function drawButton(btninfo, btncol, txtcol) {
    ctx.fillStyle=btncol;
    ctx.fillRect(btninfo.x,btninfo.y,btninfo.width,btninfo.height);
    
    ctx.fillStyle=txtcol;
    ctx.font='10pt Courier'
    ctx.fillText(btninfo.text, btninfo.x + 50, btninfo.y + 30);
}

var InstructionsButton = new Button("Instructions", 450, 200, 100, 50);
var TicTacToeButton = new Button("Tic-Tac-Toe", 450, 300, 100, 50);
var Connect4Button = new Button("Connect4", 450, 400, 100, 50);
var AboutButton = new Button("About", 450, 500, 100, 50);

drawButton(InstructionsButton,'red', 'yellow');
drawButton(Connect4Button,'blue','yellow');
drawButton(TicTacToeButton,'blue','yellow');
drawButton(AboutButton, 'red','yellow');


//adjust mouse click to canvas coordinates
function getXY(canvas, event){ 
  const rect = canvas.getBoundingClientRect();
  const y = event.clientY - rect.top;
  const x = event.clientX - rect.left;
  return {x:x, y:y};
}


function isInside(pos, rect) {
    return pos.x > rect.x && pos.x < rect.x+rect.width && pos.y < rect.y+rect.height && pos.y > rect.y;
}


document.addEventListener('click',  function (e) {
  const XY = getXY(canvas, e);
  //use the shape data to determine if there is a collision
  if(isInside(getXY(canvas, e),TicTacToeButton)) {
    window.location = "/tictactoe";
  }
  else if(isInside(getXY(canvas,e),Connect4Button)) {
      window.location = "/connect4";
  }
  else if(isInside(getXY(canvas,e),AboutButton)){
      window.location = "/about";
  }
  else if(isInside(getXY(canvas,e),InstructionsButton)){
      window.location = "/instructions";
  }
}, false);




