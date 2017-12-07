def best_moves_minimax(game, player_number, depth=1):
    '''Takes a game and returns a tuple in the form ([winning moves], [losing moves], [force tie moves], [forced tie moves])
    The parameter depth is how many moves ahead you want it to look
    When depth = 1, that's the base case. depth = 0
    
    All moves are moves the active player can take
    The proponent is the player with the given player_number
    The opponent is the player with the player number of game.get_other_player(player_number)
    
    Winning moves are moves that will allow the proponent to force a win
    Losing moves are move that will allow the opponent to force a loss for the 
    Force tie moves are moves that allow the proponent to force a tie
    Forced tie moves are moves that allow the opponent to force a tie
    Moves that don't fit into any category are just left out.
    '''
    winning_moves = []
    losing_moves = []
    force_tie_moves = []
    forced_tie_moves = []
    moves = game.get_continue_moves()
    # make sure the game isn't an end state
    if len(moves) > 0:
        test_game_infos = [(move, game.get_moved_copy(move)) for move in moves]
        # don't search any lower
        if depth == 0:
            for (move, test_game) in test_game_infos:
                winner = test_game.who_won()
                if winner is None:
                    undetermined_moves.append(move)
                elif winner == -1:
                    tying_moves.append(move)
                elif winner == player_number:
                    winning_moves.append(move)
                else:
                    losing_moves.append(move)
        else:
             
                    
            
    return (winning_moves, losing_moves, force_tie_moves, forced_tie_moves)
        
        