
let canvas = document.getElementById('canvas');

let ctx = canvas.getContext('2d');


ctx.font='30pt Georgia';
ctx.textAlign='center';

let gradient=ctx.createLinearGradient(0,0,canvas.width,0);
gradient.addColorStop("0","magenta");
gradient.addColorStop("0.5","blue");
gradient.addColorStop("1.0","black");
// Fill with gradient
ctx.fillStyle=gradient;

//ctx.fillStyle='red';

//Title
ctx.fillText('Botter Than You',500,50)



ctx.fillText('Get ready to lose!',500, 100);
ctx.font='40pt Verdana';
ctx.fillText('SELECT YOUR POISON',500, 300);



function Button(text, x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    //this.clicked = false;
    //this.hovered = false;
    this.text = text;
};

function drawButton(btn){
    
    ctx.fillRect(btn.x,btn.y,btn.width,btn.height);
    ctx.fillStyle='red';
    ctx.font= '13pt Verdana'
    ctx.fillText(btn.text, btn.x + 50, btn.y + 30);
}

var TicTacToeButton = new Button("Tic-Tac-Toe", 400, 400, 100, 50);
var Connect4Button = new Button("Connect4", 400, 550, 100, 50);


drawButton(TicTacToeButton);
drawButton(Connect4Button);


