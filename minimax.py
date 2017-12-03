# generalizable minimax algo w/ alpha beta pruning optimization



'''
convert Game states object into a tree
depends on how we're going to break this up into subproblems and utilize minimax

'''

'''
depth
nodeI
isMax
score[]
height
alpha 
beta
'''
# tree functionality lets gooooo
#TODO delete stuff like this
from anytree import Node

import monte_carlo


# returns number of children in a particular generation
# this is needs so minimax knows how many to compare

# This makes so much more sense, this is how we determine how many to compare for minimax
# idk why i thought I needed to know sibnum
#i just need to iterate through the board
def movesLeft

def sibnum(n):
    return len(n.siblings) + 1




def minimax(depth, nodeI, isMax, score, height, alpha, beta):
    # terminating, leaf node is reached
    if (depth == height):
        return score[nodeI]
        
    # if curr move is maximizer, find maximum attainable value
    
    if isMax:
        best = -1000
        
        #only works for binary, gotta fix with loop
        # loop here
            max(minimax(depth + 1, nodeI * 2, False, score, height), 
            minimax(depth + 1, nodeI * 2 + 1, False, score, height ))
    
    else:
        best = 1000
        min(minimax(depth + 1, nodeI * 2, True, score, height), 
        minimax(depth + 1, nodeI * 2 + 1, True, score, height ))
        

def unsure_monte_carlo_eval(game, unsure_rewards=[1, -1, .5], sure_rewards=[2, -2, 1.5]):
    '''Evalutates a game from player 0's perspective'''
    winner = game.who_won()
    if winner is None:
        # game is not complete
        return monte_carlo_eval(game, rewards=unsure_rewards)
    else:
        # game is complete
        return sure_rewards[winner]
    
    
def complete_minimax(game, depth, eval_func=unsure_monte_carlo_eval, ans=None):
    #TODO make depth have default
    '''
    Returns a dictionary in the form {game hash: (best move for player 0 to make in this game, expected value of that move), ...}
    where the dictionary will include all of the game hashes up to the given depth where a move could be made
    (If it's player 1's turn to move, it will swap the players so the dictionary will always be in the above form)
    We assume that the active player is making the move in the game (not player 0)
    
    This algorithm really only calculates the best move for the active player to make, then calls itself recursively on each situation it encounters
    '''
    # TODO check if it would be better if we just assumed that player 0 was making the move
    if ans is None:
        ans = {}
        
    # the information ans will contain about this game
    cur_ans_info = (None, None)    
    
    # swap so that the evaluation functions evaluate the correct player
    game = game.get_active_zero_copy()
        
    # only want moves that will continue the game
    moves = game.get_continue_moves()
    if len(moves) == 0:
        cur_ans_info = (None, eval_func(game))
    else:
        if depth == 0:
            cur_ans_info = sorted([(move, eval_func(game.get_moved_copy(move))) for move in moves], key=lambda x: x[1])[-1]
        else:
            cur_ans_info = (None, None)
            for move in moves:
                test_game = game.get_moved_copy(move)
                lower_ans = complete_minimax(test_game, depth-1, eval_func=eval_func, ans=ans)
                if cur_ans_info[1] is None:
                        cur_ans_info = (move, eval_func(test_game, depth-1, eval_func=eval_func, ans=ans))
                else:
                    
                # overwrite with values from ans
                ans = lower_ans.update(ans)
                
                lower_ans[test_game.get_hash()]
                
                    if cur_ans_info[1] is None:
                        cur_ans_info = (move, eval_func(test_game, depth-1, eval_func=eval_func, ans=ans))
                    else:
                        lower_ans = complete_minimax(game)
                        val = eval_func(test_game)
                        if val > cur_ans_info[1]:
                            cur_ans_info = (move, val)
                    
    ans[game.get_hash()] = cur_ans_info
    return ans
        
    
    
    
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
    
    
        
        
    