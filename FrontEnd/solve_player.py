from players import Player
# TODO change name
from minimax import complete_minimax
from evaluation import simple_eval

class SolvePlayer(Player):
    def __init__(self):
        self.memory = {}
        self.my_eval = lambda game, player_number : simple_eval(game, player_number, [1, -1, 0])
    
    '''Solves the current position, and then looks up the best moves from a dict'''
    def make_move(self, game):
        try:
            game.make_move(self.memory[game.get_hash()][0])
        except KeyError:
            self.memory.update(complete_minimax(game, -1, self.my_eval))
            self.make_move(game)
        
