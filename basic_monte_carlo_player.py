from players import Player, RandomPlayer
from monte_carlo import monte_carlo_eval

class BasicMonteCarloPlayer(Player):
    def __init__(self, simulation_amount, depth=0, rewards=[1, -1, .5]):
        self.simulation_amount = simulation_amount
        self.depth = depth
        # different rewards depending on which player number the player is in the game
        self.rewards = (rewards, [rewards[1], rewards[0], rewards[2]])
    
    def make_move(self, game):
        # Assumes it is making a move on its own turn
        # In order for MonteCarlo evaluation 
        # upgrade: another way of doing this would be to do the sorting in reverse, thought that runs into slight issues with the rewards being reversed; oh wait! that might work!
        
        rewards = self.rewards[game.active_player]
        poss_moves = game.get_possible_moves()
        test_games = []
        for move in poss_moves:
            test_game = game.get_copy()
            test_game.make_move(move)
            test_games.append(test_game)
            
        
        # from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        # TODO this looks like a mess, but it works
        # Sort the moves based on a Monte Carlo evaluation that flips the reward in case we're not player 0
        game.make_move([move for _, move in sorted(zip([monte_carlo_eval(test_game, rewards=rewards, simulation_amount=self.simulation_amount, depth=self.depth).value
                                                        for test_game in test_games], poss_moves))][-1])
  
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