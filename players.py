import random

class Player:
    def make_move(self, game):
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


class HumanPlayer(Player):
    def make_move(self, game):
        moves = game.get_possible_moves()
        print(game)
        while True:
            try:
                if False not in [isinstance(move, int) for move in moves]:
                    print("Moves:\n{}".format([move + 1 for move in moves]))
                    move = int(input("Type the move you'd like to do: ")) - 1
                else:
                    moves_dict = {}
                    for i, move in enumerate(moves):
                        moves_dict[i] = move
                    print("Moves:\n{}".format(moves_dict))
                    index = int(input("Type the index of the move you'd like to do: "))
                    move = moves_dict[index]
                break
            except Exception:
                print("Sorry, that didn't work.")
                
        
        game.make_move(move)
    