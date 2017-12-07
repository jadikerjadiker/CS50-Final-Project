Botter Than You by London Lowmanstone and William Yao

*Welcome to the Botter Than You DOCS by London Lowmanstone and William Yao*


Introduction:
Objective:
Botter Than You is a web application that runs a computer bot that plays two player games.

Tools:
Front End: HTML templates, CSS, Javascript, HTML5 Canvas
Backend: python Flask
Front-Back end Communication: jQuery, ajax

Functionality:
Front End: 
Uses 5 HTML templates, 3 Javascript files and 2 css stylesheets. The HTML templates use the CSS stylesheets and
render the canvas on the page.

Backend: 
Minimax algorithm is used to solve tic-tac-toe upon launch of the application. 
Monte Carlo algorithm and position evaluation function, which optimizations is used to inform the 
connect4 player using simulations.


#talk generally about design of project, inspiration for project functionality, Generalizability, goals etc.

Files:
Front End:
static folder:
    logos folder:
    Contains png files that are used throughout the project
    BotterThanYou.PNG is used on the homepage, see index.html template
    Connect4.PNG is used on the connect4 page, see connect4.js
    Tic-Tac-Toe.PNG is used on the tictactoe page, see tictactoe.js
    
    .js files
    connect4.js
        javascript for connect4 game page
    index.js
        javascript for homepage
    indexstyle.css
        css styling for homepage, taken from https://bootswatch.com/
    style.css
        css styling for other pages, taken from https://bootswatch.com/
    
    tictactoe.js
        javascript for tictactoe game page
templates folder:
    Contains html templates that are used within the project
    about.html
        html template for the about page, uses style.css
    connect4.html
        html template for the connect4 game page, uses style.css
    index.html
        html template for the homepage, uses indexstyle.css
    instructions.html
        html template for the instruction manual, uses style.css
    tictactoe.html
        html templaet for the tictactoe game page, uses style.css


Back End:

advised_monte_carlo_player.py:
TODO

application.py:
Drivers the Flask app

connect_four.py:
Game class for connect4

evaluation.py:
TODO

game.py:
General Game class, tictactoe and connect4 classes inherit this class

minimax.py:
Generalizable implementation of the minimax algorithm

monte_carlo_evaluation.py:
TODO

performance_testers.py:
TODO

players.py:
TODO

position_eval.py:
TODO

solve_play.py:
TODO

tic_tac_toe.py:
Game class for tic-tac-toe

useful_functions.py:
TODO



