# generalizable minimax

def complete_minimax(game, depth, eval_func, player_number=None, ans=None):
    #TODO make depth have default
    '''
    Returns a dictionary in the form {game hash: (best move for the active player to make in this game, expected value of that move), ...}
    where the dictionary will include all of the game hashes up to the given depth where a move could be made
    We assume that the active player is making the move in the game (not player 0)
    
    This algorithm really only calculates the best move for the active player to make, then calls itself recursively on each situation it encounters
    '''
    if player_number is None:
        player_number = game.active_player
    
    # TODO check if it would be better if we just assumed that player 0 was making the move
    if ans is None:
        ans = {}
        
    # the information ans will contain about this game
    best_move = None
    expected_value = None

    # only want moves that will continue the game
    moves = game.get_continue_moves()
    if len(moves) == 0:
        expected_value = eval_func(game, player_number=player_number)
    else:
        # figure out if we're maximizing or minimizing
        if game.active_player == player_number:
            min_or_max = max
        else:
            min_or_max = min
        if depth == 0:
            # calculate the best move and the expected value for the original player
            best_move, expected_value = min_or_max([(move, eval_func(game.get_moved_copy(move), player_number=player_number)) for move in moves], key=lambda x: x[1])
        else:
            test_games = []
            for move in moves:
                test_game = game.get_moved_copy(move)
                test_games.append((move, test_game.get_hash()))
                lower_ans = complete_minimax(test_game, depth-1, eval_func=eval_func, player_number=player_number, ans=ans)
                # keep the same values in ans while adding in the new ones
                lower_ans.update(ans)
                ans = lower_ans
            best_move, expected_value = min_or_max([(test_game_info[0], ans[test_game_info[1]][1]) for test_game_info in test_games], key=lambda x: x[1])
            # TODO delete
            # print("best move for {}is {}\n".format(hash_to_game(game.get_hash()), best_move))
                
    ans[game.get_hash()] = (best_move, expected_value)
    return ans
    

if __name__ == "__main__":
    from tic_tac_toe import TicTacToe
    from monte_carlo_evaluation import unsure_monte_carlo_eval
    t = TicTacToe()
    t.make_move(0)
    t.make_move(1)
    t.make_move(3)
    t.make_move(2)
    #t.make_move(7)
    #t.make_move(5)
    #t.make_move(7)
    #t.make_move(4)
    print(t)
    print("'{}'".format(t.get_hash()))
    ans = complete_minimax(t, -1, unsure_monte_carlo_eval)
    print(ans)
    print(len(ans))
    print(t.get_complexity(-1))
    print(ans[t.get_hash()])
