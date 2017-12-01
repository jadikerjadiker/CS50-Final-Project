def minimax(game):
    def eval_game(game):
        '''Evaluate an end state, assuming player 0 made the last move to end the game
        If the game is not an end state (game.who_won() == None) then return None
        '''
        winner = game.who_won()
        if winner:
            # not complete 
            
            
    
    '''
    Takes a Game object and returns a dictionary where the keys are the hash values for game states, and the value is the best move to make in that position.
    Assumes that all wins are equal and all losses are equal and all ties are in between the two and equal.
    '''
    
    ans = {}
    