
// set up HTML5 canvas and context
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');


// Creates color gradient, for aesthetic use
let gradient=ctx.createLinearGradient(0,0,canvas.width,0);
gradient.addColorStop("0","magenta");
gradient.addColorStop("0.5","blue");
gradient.addColorStop("1.0","red");

// Sets inital context properties
ctx.fillStyle=gradient;
ctx.textAlign='center';

// Text class with useful attributes
function Text(text, x, y) {
  this.text = text;
  this.x=x;
  this.y=y;
}

// Button class with useful attributes
function Button(text, x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    //this.clicked = false;
    //this.hovered = false;
    this.text = text;
};

// function to draw text on canvas, ar
function drawText(txtinfo, txtcolor, txtsizefont) {
  ctx.strokeStyle=txtcolor;
  ctx.font = txtsizefont;
  ctx.strokeText(txtinfo.text,txtinfo.x,txtinfo.y);
  
}

// function to draw buttons on canvas
function drawButton(btninfo, btncol, txtcol) {
    ctx.fillStyle=btncol;
    ctx.fillRect(btninfo.x,btninfo.y,btninfo.width,btninfo.height);
    
    ctx.fillStyle=txtcol;
    ctx.font='10pt Courier'
    ctx.fillText(btninfo.text, btninfo.x + 50, btninfo.y + 30);
}

// Creates instances of texts and buttons and draws on canvas
var subtitle = new Text("Get ready to lose!", 500, 130);
drawText(subtitle, 'white','30pt Courier');

var InstructionsButton = new Button("Instructions", 450, 200, 100, 50);
var TicTacToeButton = new Button("Tic-Tac-Toe", 450, 300, 100, 50);
var Connect4Button = new Button("Connect4", 450, 400, 100, 50);
var AboutButton = new Button("About", 450, 500, 100, 50);

drawButton(InstructionsButton,'red', 'white');
drawButton(Connect4Button,'blue','white');
drawButton(TicTacToeButton,'blue','white');
drawButton(AboutButton, 'red','white');


// Gets x, y coordinates of mouse on canvas
function getXY(canvas, event){ 
  const rect = canvas.getBoundingClientRect();
  const y = event.clientY - rect.top;
  const x = event.clientX - rect.left;
  return {x:x, y:y};
}

/* Function that takes in an x, y position and a rectangular shape
   Determines if the pos is contained within the rectangle
*/
function isInside(pos, rect) {
    return pos.x > rect.x && pos.x < rect.x+rect.width && pos.y < rect.y+rect.height && pos.y > rect.y;
}

// Mouse click event listener to redirect to other pages based on button click
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




