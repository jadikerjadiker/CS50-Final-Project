from evaluation import Evaluation

class PositionEvaluation(Evaluation):
    # TODO document
    '''
    results is a set containing any of 0, 1, 2, or 3
    "the player" is the player whose player number is player_number
    0 means the player can win from this position
    1 means the opponent can win from this position
    2 means the player can force a tie from this position
    3 means the opponent can force a tie from this position
    
    player_number is the number of the player that the results are for
    rewards is to allow this to actually be a subclass of Evaluation and have a value
    rewards is in the form [points for win, points for loss, points for force tie, points for forced tie, points for undetermined]
    '''
    def __init__(self, results, player_number, rewards=(2, -2, 1.5, 0, 0)):
        self.results = results
        self.player_number = player_number
        self.rewards = rewards
        super().__init__(self.compute_value())
        
    def compute_value(self):
        if self.win():
            return self.rewards[0]
        elif self.lose():
            return self.rewards[1]
        elif self.force_tie():
            return self.rewards[2]
        elif self.forced_tie():
            return self.rewards[3]
        else:
            return self.rewards[4]
        
    def win(self):
        return 0 in self.results
    
    def lose(self):
        return 1 in self.results
        
    def force_tie(self):
        return 2 in self.results
        
    def forced_tie(self):
        return 3 in self.results
        
    def __str__(self):
        return "<PositionEvaluation object with results: {}>".format(self.results)

def position_eval(game, player_number, depth, rewards=(2, -2, 1.5, 0, 0)):
    '''
    Returns a PositionEvaluation object
    TODO document better
    
    '''
    
    def any_one(evaluations, value):
        '''
        Returns whether or not any one of the evaluations has the given value in its results
        '''
        for e in evaluations:
            if value in e.results:
                return True
        return False
        
    def all_ones(evaluations, value):
        '''
        Returns whether or not all of the evaluations has the given value in their results
        '''
        for e in evaluations:
            if value not in e.results:
                return False
        return True
        
        
    # TODO make a default for depth
    '''
    ans is a set containing any of the numbers 0, 1, 2, or 3
    "the player" is the player whose player number is player_number
    0 means the player can win from this position
    1 means the opponent can win from this position
    2 means the player can force a tie from this position
    3 means the opponent can force a tie from this position
    
    If more than one of these things is true, ans will contain more than one of those numbers
    '''
    ans = set()
    if depth == 0:
        winner = game.who_won()
        # undetermined games don't fit in any category
        if winner is not None:
            if winner == -1:
                # this could be either a force tie or forced tie, so add both
                ans.add(3)
                ans.add(4)   
            elif winner == player_number:
                # win
                ans.add(0)
            else:
                # loss; winner is opponent
                ans.add(1)
    else:
        lower_level = [position_eval(lower_game, player_number, depth-1, rewards) for lower_game in game.get_next_level()]
        any_or_all = [lambda v: any_one(lower_level, v), lambda v: all_ones(lower_level, v)]
        if game.active_player != player_number:
            # if the player we're evaluating is not the active player, whether or not we're looking for any or all reverses
            # for example, when the opponent is making the move, "if any future positions are wins, this position is a win" becomes
            #..."if all future positions are wins, this position is a win"
            # ...because unless all of the positions are wins for the main player, the opponent could just choose another path
            any_or_all.reverse()
        # if any future positions are wins, this position is a win
        if any_or_all[0](0):
            ans.add(0)
        # if all future positions are losses, this position is a loss
        if any_or_all[1](1):
            ans.add(1)
        # if any future positions are force ties, this position is a force tie
        if any_or_all[0](3):
            ans.add(3)
        # if all future positions are forced ties, this position is a forced tie
        if any_or_all[1](4):
            ans.add(4)
        
    return PositionEvaluation(ans, player_number, rewards)
    
    


if __name__ == "__main__":
    from tic_tac_toe import TicTacToe
    
    t = TicTacToe()
    t.make_move(0)
    t.make_move(1)
    t.make_move(3)
    t.make_move(2)
    #t.make_move(6)
    
    print(position_eval(t, player_number=1, depth=1))
            
