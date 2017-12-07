from position_eval import position_eval
from monte_carlo_evaluation import monte_carlo_eval
from players import Player

class AdvisedMonteCarloPlayer(Player):
    '''
    A basic monte carlo player that takes certain wins and ties and avoids certain
    '''
    def __init__(self, mc_simulation_amount, mc_depth, pe_depth, mc_rewards=(1, -1, .5), pe_rewards=(2, -2, .9, 0, 0)):
        self.mc_simulation_amount = mc_simulation_amount
        self.mc_depth = mc_depth
        self.mc_rewards = mc_rewards
        self.pe_depth = pe_depth
        self.pe_rewards = pe_rewards
        # use position_eval with the specified depth to advi
        # TODO see if these actually work - delete them!
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
        # TODO potentially delete lower level thing
        ep_scores = [position_eval(test_game, main_player, self.pe_depth-1, self.pe_rewards).value for test_game in test_games]
        mc_scores = [self.monte_carlo_func(test_game, main_player).value for test_game in test_games]
        # from https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        # sort the moves first based on their position evaluation score, and then based on their monte carlo score
        sorted_moves = sorted([(moves[i], (ep_scores[i], mc_scores[i])) for i in range(len(moves))], key=lambda x: x[1])

        # from https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        # Sort the moves based on a Monte Carlo evaluation
        
        game.make_move(sorted_moves[-1][0])
        
if __name__ == "__main__":
    from performance_testers import test_against
    from monte_carlo_evaluation import unsure_monte_carlo_eval
    from evaluation import Evaluation, simple_eval
    from connect_four import ConnectFour
    from tic_tac_toe import TicTacToe
    from old_minimax import complete_minimax
    from players import RandomPlayer, HumanPlayer
    from basic_monte_carlo_player import BasicMonteCarloPlayer
    def my_eval(game, player_number):
        #unsure_monte_carlo_eval(game, player_number, unsure_rewards=[1, -1, .5], sure_rewards=[2, -2, 1.5], main_player=RandomPlayer(), simulation_amount=5, depth=0, opponent=RandomPlayer()):
        
        return unsure_monte_carlo_eval(game, player_number, simulation_amount=3)
        '''
        winner = game.who_won()
        if winner is None:
            return Evaluation(0)
        else:
            return simple_eval(game, player_number, [2, -2, 1.5])
        '''
        
    def my_index(game, player_number):
        ans = complete_minimax(game, 4, my_eval)
        print([(index, ans[index][0], ans[index][1].value) for index in ans])
        return ans
    
    # With my_index = complete_minimax(game, 4, my_eval) and my_eval = unsure_monte_carlo_eval(game, player_number, simulation_amount=3)
    # Score 0 - 2 - 0. It's bad and slow. Not a good combo.
    # test_against((IndexPlayer(my_index), BasicMonteCarloPlayer(5, 2)), ConnectFour, comment=6)
    
    test_against((AdvisedMonteCarloPlayer(5, 2, 4), BasicMonteCarloPlayer(5, 2)), ConnectFour, comment=6)