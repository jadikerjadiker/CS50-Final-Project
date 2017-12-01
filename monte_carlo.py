import players
from evaluation import Evaluation

class MonteCarloEvaluation(Evaluation):
    def __init__(self, value, simulations):
        super().__init__(value)
        self.simulations = simulations
        
def monte_carlo_eval(original_game, main_player, rewards, sim_amt=100, opponent=players.RandomPlayer()):
    '''Returns a MonteCarloEvaluation object
    Plays random games from the given game position and averages the results
    Assumes that player has player number 0 in the game
    
    original_game is the game to simulate from
    main_player is a Player object that we use to simulate games; should be player 0 in the game
    rewards is a tuple: (points for winning, points for losing, points for tying)
    sim_amt is how many games to simulate
    opponent is the other Player object we use to simulate games; should be player 1 in the game
    '''
        
    value = 0
    for i in range(sim_amt):
        # TODO make it keep track of places it has already simulated and simulate places it's less certain about
        game = original_game.get_copy()
        players = (main_player, opponent)
        
        while game.who_won() is None:
            players[game.active_player].make_move(game)
        
        # update the value    
        value += rewards[game.who_won()]
        
    return MonteCarloEvaluation(value / sim_amt, sim_amt)
    
    
if __name__ == "__main__":
    from tic_tac_toe import TicTacToe
    from players import RandomPlayer
    import random
    
    g = TicTacToe()
    player = RandomPlayer()
    for i in range(100):
        print(monte_carlo_eval(g, player, [1, -1, 0], 10000))
    