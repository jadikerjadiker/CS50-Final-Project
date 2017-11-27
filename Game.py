#from abc import abstractmethod # TODO not sure if needed

class State:
    def __init__(self, hash, whoWon, properties):
        self.hash = hash
        self.whoWon = whoWon
        self.properties = properties
        
class Game():
    @classmethod
    def other_player(cls, player):
        '''Returns the number of the other player (either a 0 or 1)'''
        return (player + 1) % 2
        
    '''
    TODO documentation
    '''
    def __init__(self, state_and_player=None):
        if state_and_player is None:
            self.state, self.active_player = self.get_initial_state()
        else:
            self.state, self.active_player = state_and_player
    
    def get_next_level(self):
        '''Return a list of all the games that can be reached with one action from the current game'''
        ans = []
        actions = self.get_continue_actions()
        for action in actions:
            copy = self.get_copy()
            copy.make_move(action)
            ans.append(copy)
        return ans
    
    def get_complexity(self, depth):
        '''Determines the number of possible final states a game has with a depth search of size depth
        If you want the total complexity, use depth=-1
        TODO this does not work yet for games with repeated states, such as Chopsticks
        '''
        if depth == 1:
            # if you have no descendants, return 1 since you're the only final state
            return len(self.get_next_level()) or 1
        elif depth != 0:
            next_level = self.get_next_level()
            if len(next_level) == 0:
                # this is the only final state here
                return 1
            else:
                # return the number of final states of your descendants
                return sum([game.get_complexity(depth-1) for game in next_level])
        else:
            return 0
    
    def get_continue_actions(self):
        '''Like get_possible_actions, except it only gets the actions if the game is not complete
        Removes the undefined behavior allowed in get_possible_actions
        '''
        if self.who_won() is None:
            return self.get_possible_actions()
        else:
            return []
    
    def get_initial_state(self):
        raise NotImplementedError
    
    def get_properties(self):
        '''This returns a list of numbers of constant length describing the state and active player of the game, or None
        This is what we'd feed into a neural net to learn about the game
        '''
        raise NotImplementedError
        
    def get_copy(self):
        '''Return a copy of the object'''
        raise NotImplementedError
    
    def get_hash(self):
        '''Return a unique string for the state and active player'''
        raise NotImplementedError
    
    def get_possible_actions(self):
        '''Return a list of the possible actions that can be taken by self.active_player in the self.state state
        Behavior is undefined when the game is complete
        '''
        raise NotImplementedError
        
    def make_move(self, action):
        '''Change the state of the game and update the active player based on the action'''
        raise NotImplementedError
        
    def who_won(self):
        '''Return 0 if player 0 won, 1 if player 1 won, -1 if there was a tie, and None if the game has not finished'''
        raise NotImplementedError
        

if __name__ == "__main__":
    from TicTacToe import TicTacToe
    print("Working...")
    print("Number of end states in TicTacToe: {}".format(TicTacToe().get_complexity(-1)))