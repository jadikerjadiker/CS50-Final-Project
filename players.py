import random

class Player:
    def make_move(game):
        '''Make a move in the game (a Game object)'''
        raise NotImplementedError
        
    def __str__(self):
        "<Player object>"
        
        
class RandomPlayer(Player):
    @classmethod
    def get_random_game(cls, game_cls):
        '''Returns a random game of the class game_cls which must be a subclass of Game'''
        game = game_cls()
        while game.who_won() is None:
            game.make_move(random.choice(game.get_possible_moves()))
        return game
    
    def make_move(self, game):
        game.make_move(random.choice(game.get_possible_moves()))
        
    def __str__(self):
        return "<RandomPlayer object>"
        
        
class BasicMonteCarloPlayer(Player):
    