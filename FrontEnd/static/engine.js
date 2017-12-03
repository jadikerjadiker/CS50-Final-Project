//this is funky stufs


var GameEngine = function(canvas, FPS) {
    this.FPS = 1000 / FPS;
    this.canvas = canvas;
    this.context2D = canvas.getContext("2d");
    this.gameObjects = [];
    this.setupCanvas();
};


GameEngine.prototype.setupCanvas = function() {
    this.context2D.textBaseline = "top";
    this.context2D.mouse = {
        x: 0,
        y: 0,
        clicked: false,
        down: false
    };
 
    var engine = this;
 
    this.canvas.addEventListener("mousemove", function(e) {
        engine.context2D.mouse.x = e.offsetX;
        engine.context2D.mouse.y = e.offsetY;
        engine.context2D.mouse.clicked = (e.which == 1 &amp; &amp; !engine.context2D.mouse.down);
        engine.context2D.mouse.down = (e.which == 1);
    });
 
    this.canvas.addEventListener("mousedown", function(e) {
        engine.context2D.mouse.clicked = !engine.context2D.mouse.down;
        engine.context2D.mouse.down = true;
    });
 
    this.canvas.addEventListener("mouseup", function(e) {
        engine.context2D.mouse.down = false;
        engine.context2D.mouse.clicked = false;
    });
} 



GameEngine.prototype.run = function() {
    var desiredTime = Date.now() + this.FPS;
 
    this.update();
    this.draw();
 
    var interval = Math.max(0, desiredTime-Date.now());
    setTimeout(_.bind(this.run, this), interval);
}