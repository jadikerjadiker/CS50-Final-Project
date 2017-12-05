class Evaluation:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return "<Evaluation object of value: {}>".format(self.value)
        
def simple_eval(game, player_number, rewards):
    '''Evaluates an end game'''
    return winner_eval(game.who_won(), player_number, rewards)
    
def winner_eval(winner_number, player_number, rewards):
    '''Computes the reward based on who won and who the player is'''
    if winner_number is not None:
        if player_number == 0:
            player_rewards = rewards
        else:
            player_rewards = (rewards[1], rewards[0], rewards[2])
            
        return Evaluation(player_rewards[winner_number])
    else:
        return Evaluation(None)