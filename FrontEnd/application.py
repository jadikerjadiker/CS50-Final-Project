import os
import random
import time

from flask import Flask, render_template, redirect, request, jsonify
from tic_tac_toe import TicTacToe
from connect_four import ConnectFour
from basic_monte_carlo_player import BasicMonteCarloPlayer
from advised_monte_carlo_player import AdvisedMonteCarloPlayer
from solve_player import SolvePlayer

app = Flask(__name__)
    
game = TicTacToe()
tic_tac_toe_bot = SolvePlayer()
# have the bot solve tic tac toe on startup
# TODO turn this back on
# tic_tac_toe_bot.make_move(TicTacToe())

bot = BasicMonteCarloPlayer(10, 1)
moving = False

# from CS50
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("index.html")
    

@app.route("/tictactoe", methods=["GET"])
def tictactoe():
    global game, bot, moving
    moving = False
    game = TicTacToe()
    game.active_player = random.choice([0, 1])
    # use the bot that has memorized all the best moves
    bot = tic_tac_toe_bot
    return render_template("tictactoe.html", player = game.active_player)
    
@app.route("/connect4", methods = ["GET", "POST"])
def connect4():
    global game, bot, moving
    moving = False
    game = ConnectFour()
    game.active_player = random.choice([0, 1])
    bot = AdvisedMonteCarloPlayer(7, 2, 4)
    return render_template("connect4.html", player = game.active_player)

@app.route("/human_move", methods=["POST"])
def make_human_move():
    global moving
    # bot_move is 1 if the javascript should request a bot move
    # bot_move is 0 if the javascript should not request a bot move
    bot_move = 0
    print("human move, moving is:")
    print(moving)
    # make sure a move is not currently going on
    if not moving:
        moving = True
        move = request.form.get("move")
        # deal with race condition of a person clicking multiple times quickly
        if move:
            move = int(move)
            # make sure it really is the player's turn
            if game.active_player == 0:
                if move in game.get_continue_moves():
                    game.make_move(move)
                    if game.who_won() is None:
                        bot_move = 1
                        # It's okay if we continue to say we're "moving" when the game is done
                else:
                    # no move was actually made
                    moving = False
                    
        
    json_dict = game.get_json_dict()
    json_dict["bot_move"] = bot_move
    return jsonify(json_dict)
    
@app.route("/bot_move", methods=["POST"])
def make_bot_move():
    global moving
    moving = True
    print("I'm making a bot move!")
    bot.make_move(game)
    time.sleep(1)
    moving = False
    return jsonify(game.get_json_dict())
    
@app.route("/about", methods = ["GET", "POST"])
def aboutpage():
    return render_template("about.html")
    
@app.route("/instructions", methods = ["GET", "POST"])
def instructionspage():
    return render_template("instructions.html");

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))