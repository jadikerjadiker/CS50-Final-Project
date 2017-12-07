from position_eval import position_eval
from monte_carlo_evaluation import monte_carlo_eval
from players import Player

class AdvisedMonteCarloPlayer(Player):
    '''
    A basic monte carlo player that takes certain wins and ties and avoids certain
    '''
    def __init__(self, mc_simulation_amount, mc_depth, pe_depth, mc_rewards=(1, -1, .5), pe_rewards=(2, -2, 1.5, 0)):
        self.mc_simulation_amount = mc_simulation_amount
        self.mc_depth = mc_depth
        self.mc_rewards = mc_rewards
        self.pe_depth = pe_depth
        self.pe_rewards = pe_rewards
        # use position_eval with the specified depth to advi
        self.advise_func = lambda game, player_number, lower_level=None: position_eval(game, player_number, self.pe_depth,
                                                                                       self.pe_rewards, lower_level)
        self.monte_carlo_func = lambda game, player_number: monte_carlo_eval(game, player_number, rewards=self.mc_rewards,
                                                              simulation_amount=self.mc_simulation_amount, depth=self.mc_depth)
        
    def make_move(self, game):
        # TODO fix design. This could be beautiful
        main_player = game.active_player
        # Assumes it is making a move on its own turn
        moves = game.get_possible_moves()
        test_games = [game.get_moved_copy(move) for move in moves]
        lower_level = [position_eval(test_game, active_player, depth-1, rewards) for lower_game in game.get_next_level()]
            
        # from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        # Sort the moves based on a Monte Carlo evaluation
        scores = [self.monte_carlo_func(test_game).value for test_game in test_games]
        moves = [ sorted()
        game.make_move(max(zip(scores, poss_moves))[1])
        
