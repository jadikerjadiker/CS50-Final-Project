from players import Player

class IndexPlayer(Player):
    def __init__(self, index_func):
        self.index_func = index_func
        self.predetermined = {}
    
    def make_move(self, game):
        # TODO document
        self.add_predetermined(self.index_func(game, player_number=game.active_player))
        game.make_move(self.predetermined[game.get_hash()][0])
        
    def add_predetermined(self, more):
        # a template for subclasses to override
        # completely overwrites matching values in self.predetermined with new values from more
        self.predetermined.update(more)
        
if __name__ == "__main__":
    from performance_testers import test_against
    from monte_carlo_evaluation import unsure_monte_carlo_eval
    from evaluation import Evaluation, simple_eval
    from connect_four import ConnectFour
    from tic_tac_toe import TicTacToe
    from minimax import complete_minimax
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
    
    test_against((IndexPlayer(my_index), BasicMonteCarloPlayer(5, 2)), ConnectFour, comment=6)