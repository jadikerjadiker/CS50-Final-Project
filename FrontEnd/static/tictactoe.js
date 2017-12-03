
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');


ctx.textAlign='center';

let gradient=ctx.createLinearGradient(0,0,canvas.width,0);
gradient.addColorStop("0","magenta");
gradient.addColorStop("0.5","blue");
gradient.addColorStop("1.0","black");

ctx.fillStyle=gradient;


//Title



function Text(text, x, y) {
  this.text = text;
  this.x=x;
  this.y=y;
};

var title = new Text("Tic-Tac-Toe", 500, 50);

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
  ctx.fillStyle=txtcolor;
  ctx.font = txtsizefont;
  ctx.fillText(txtinfo.text,txtinfo.x,txtinfo.y);
  
}

drawText(title, gradient, '50pt Verdana');


function drawButton(btninfo, btncol, txtcol) {
    ctx.fillStyle=btncol;
    ctx.fillRect(btninfo.x,btninfo.y,btninfo.width,btninfo.height);
    
    ctx.fillStyle=txtcol;
    ctx.font='13pt Verdana'
    ctx.fillText(btninfo.text, btninfo.x + 50, btninfo.y + 30);
}


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
  
  
}, false);


