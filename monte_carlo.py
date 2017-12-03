from players import RandomPlayer
from evaluation import Evaluation

class MonteCarloEvaluation(Evaluation):
    def __init__(self, value, simulations):
        super().__init__(value)
        self.simulations = simulations
        
    def __str__(self):
        return "MonteCarloEvaluation object with value: {} from {} simulations".format(self.value, self.simulations)
    

def monte_carlo_eval(original_game, main_player=RandomPlayer(), rewards=[1, -1, .5], simulation_amount=100, depth=0, opponent=RandomPlayer()):
    '''Returns a MonteCarloEvaluation object
    Plays random games from the given game position and averages the results
    Assumes that player has player number 0 in the game
    
    original_game is the game to simulate from
    main_player is a Player object that we use to simulate games; should be player 0 in the game
    rewards is a tuple: (points for winning, points for losing, points for tying)
    simulation_amount is how many games to simulate per possible game at the specified depth
    depth is how many layers down you want it to start simulating
    opponent is the other Player object we use to simulate games; should be player 1 in the game
    '''
        
    if depth==0:
        value = 0
        for _ in range(simulation_amount):
            # TODO make it keep track of places it has already simulated and simulate places it's less certain about
            game = original_game.get_copy()
            players = (main_player, opponent)
            
            while game.who_won() is None:
                players[game.active_player].make_move(game)
            
            # update the value    
            value += rewards[game.who_won()]
            
        return MonteCarloEvaluation(value / simulation_amount, simulation_amount)
    else:
        winner = original_game.who_won()
        if winner is None:
            # list of MonteCarloEvaluation objects for each
            lower_level = [monte_carlo_eval(game, main_player, rewards, simulation_amount, depth-1, opponent) for game in original_game.get_next_level()]
                
            return MonteCarloEvaluation(sum([e.value for e in lower_level]) / len(lower_level), sum([e.simulations for e in lower_level]))
        else:
            return MonteCarloEvaluation(rewards[winner], 1)
    
    
if __name__ == "__main__":
    from tic_tac_toe import TicTacToe
    from connect_four import ConnectFour
    from players import RandomPlayer
    import random
    
    g = TicTacToe()
    g = ConnectFour()
    player = RandomPlayer()
    for i in range(100):
        print(monte_carlo_eval(g, player, [1, -1, 0], 5, 3))
        print(monte_carlo_eval(g, player, [0, 0, 1], 5, 3))