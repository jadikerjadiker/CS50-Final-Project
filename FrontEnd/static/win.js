
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');


ctx.textAlign='center';

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

var title = new Text("YOU WON!!", 500, 200);

function Button(text, x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    //this.clicked = false;
    //this.hovered = false;
    this.text = text;
};

var backButton = new Button("BACK",100, 700, 100, 50);


function drawText(txtinfo, txtcolor, txtsizefont) {
  ctx.fillStyle=txtcolor;
  ctx.font = txtsizefont;
  ctx.fillText(txtinfo.text,txtinfo.x,txtinfo.y);
  
}

drawText(title, gradient, '100pt Verdana');


function drawButton(btninfo, btncol, txtcol) {
    ctx.fillStyle=btncol;
    ctx.fillRect(btninfo.x,btninfo.y,btninfo.width,btninfo.height);
    
    ctx.fillStyle=txtcol;
    ctx.font='13pt Verdana'
    ctx.fillText(btninfo.text, btninfo.x + 50, btninfo.y + 30);
}

drawButton(backButton, "yellow", "blue");

//****maybe include image or something*****


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
  
  if(isInside(getXY(canvas, e), backButton)) {
    alert("going back to homepage!");
    window.location = "/";
  }
    
  
}, false);


