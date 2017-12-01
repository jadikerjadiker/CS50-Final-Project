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
from anytree import Node


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
    
    if (isMax):
        
        best = -1000
        
        #only works for binary, gotta fix with loop
        for i in range(sibnum())
        
            max(minimax(depth + 1, nodeI * 2, False, score, height), 
            minimax(depth + 1, nodeI * 2 + 1, False, score, height ))
    
    else:
        min(minimax(depth + 1, nodeI * 2, True, score, height), 
        minimax(depth + 1, nodeI * 2 + 1, True, score, height ))
        
    