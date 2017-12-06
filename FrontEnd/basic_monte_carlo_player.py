from players import Player, RandomPlayer
from monte_carlo_evaluation import monte_carlo_eval

class BasicMonteCarloPlayer(Player):
    def __init__(self, simulation_amount, depth=0, rewards=(1, -1, .5)):
        self.simulation_amount = simulation_amount
        self.depth = depth
        # different rewards depending on which player number the player is in the game
        self.rewards = rewards
    
    def make_move(self, game):
        # TODO delete
        from useful_functions import p_r
        
        # Assumes it is making a move on its own turn

        poss_moves = game.get_possible_moves()
        test_games = []
        for move in poss_moves:
            test_game = game.get_copy()
            test_game.make_move(move)
            test_games.append(test_game)
            
        
        # from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        # Sort the moves based on a Monte Carlo evaluation
        scores = [monte_carlo_eval(test_game, player_number=game.active_player, rewards=self.rewards,
                                   simulation_amount=self.simulation_amount, depth=self.depth).value 
                  for test_game in test_games]
                  
        game.make_move(max(zip(scores, poss_moves))[1])
  
if __name__ == "__main__":
    from tic_tac_toe import TicTacToe
    from players import RandomPlayer
    g = TicTacToe()
    players = (BasicMonteCarloPlayer(1000), RandomPlayer())
    while g.who_won() is None:
        print(g)
        print()
        players[g.active_player].make_move(g)
        
    print(g)
    if g.who_won() == -1:
        print("Tie!")
    else:
        print("Player {} won!".format(g.who_won()))