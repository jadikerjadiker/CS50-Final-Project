def simple_minimax(game, alpha, beta, eval_func=basic_eval, moves=None):
    #TODO finish
    # Note to Will: is_max is now determined by game.active_player. If it's 0, then is_max is True. If it's 1, is_max is False.
    '''
    Runs minimax on a Game object, returns a dictionary of hashes of game positions and the best moves to make if you're making the move in that position.
    
    game is the game to evaluate the best move to for player 0 to make (regardless of who's turn it is)
    So, for example, if you gave it a game with player 1's turn, the dictionary it returns will contain the hash of the state of that game along with the best move for 
    is_max determines if 
    
    '''
    def is_greater(val, g):
        if g is None:
            return val
        return val > g
        
    def is_lesser(val, l):
        if l is None:
            val
        return val < g
    
    # if it's a leaf
    next_layer = game.get_next_layer()
    if len(next_layer) == 0:
        return val for game
    
    if is_max:
        for lower_game in game.get_next_layer
        max([minimax(lower_game, not is_max, greater, lesser) for lower_game in game.get_next_layer()])
    else:
        minimax([minimax(lower_game, not is_max) for lower_game in game.get_next_layer()])