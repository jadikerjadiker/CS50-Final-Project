class IndexPlayer(Player):
    def __init__(self, eval_func):
        self.eval_func = eval_func
        self.predetermined = {}
    
    def make_move(self, game):
        for move in game.get_possible_moves():
            