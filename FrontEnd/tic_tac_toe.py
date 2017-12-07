'''
By London Lowmanstone
Class for the game Tic-tac-toe
'''

from game import Game

class TicTacToe(Game):
    '''
    TODO documentation
    '''
    def get_initial_state(self):
        # return an empty board
        return [-1] * 9
    
    def get_state_hash(self):
        string_list = ["O", "X", " "]
        ans = ""
        for val in self.state:
            ans += string_list[val]
        return ans
    
    def get_json_dict(self):
        # the dictionary we will return
        ans = {}
        # iterate through each slot on the board
        for i, val in enumerate(self.state):
            # the key is the number of the slot
            # the value is the player who moved in that slot
            ans[str(i)] = val
        # add the active player key and value
        ans["active_player"] = self.active_player
        # add the winner key and value
        winner = self.who_won()
        if winner is None:
            ans["winner"] = -2
        else:
            ans["winner"] = winner
        
        # return the result
        return ans
            
    def swap_players(self):
        self.state = [Game.get_other_player(val) if val >= 0 else -1 for val in self.state ]
    
    def get_copy(self):
        return TicTacToe((self.state[:], self.active_player))
    
    def get_possible_moves(self):
        return [i for i in range(len(self.state)) if self.state[i] == -1]
        
    def make_move(self, action):
        self.state[action] = self.active_player
        self.active_player = Game.get_other_player(self.active_player)
        
    def who_won(self):
        '''returns 0 if player 0 won, 1 if player 1 won, -1 if it's a tie and None if it's unfinished'''
        '''TODO fix inline comments'''
        if -1 in self.state:
            # game is not done, default to unfinished
            ans = None
        else:
            # game is done, default to tie
            ans = -1
            
        # the current player number we're checking to see if they won
        player = None
        '''
        When checking is 0 we check rows
        When checking is 1 we check columns
        When checking is 2 we check top left diagonal
        When checking is 3 we check top right diagonal
        '''
        # TODO this could probably be done better
        for checking in range(4):
            # the number of the symbol in the series we're looking for
            for i in range(3):
                if checking < 2:
                    #checking rows and columns
                    for j in range(3):
                        if checking == 0:
                            # checking rows
                            # iterate through the row
                            val = self.state[i * 3 + j]
                        else:
                            # checking columns
                            # iterate through the column
                            val = self.state[i + j * 3]
                        
                        if val == -1: # person doesn't have the entire row or column
                            break
                        else:
                            # if it just started checking this line
                            if j == 0: 
                                # whoever has the first space must have the other two to win
                                player = val
                            # if the player doesn't have a win
                            elif not val == player:
                                break
                            # if the player does have a win
                            elif j==2:
                                return player
                else: #checking diagonals
                    if checking==2:
                        val = self.state[i * 4]  # want it to check slots 0, 4, 8
                    else: #checking==3
                        val = self.state[(i+1)*2]  # want it to check slots 2, 4, 6
                        
                    if val == -1: #person doesn't have the row or column
                        break
                    else:
                        if i == 0: #if we just started checking this diagonal
                            # whoever has the first space must have the other two to win
                            player = val
                        elif not val == player:  # if the player doesn't have a win
                            break
                        elif i == 2:
                            # if the player does have a win
                            return player
        return ans
       
    def __str__(self):
        if self.active_player == 0:
            this = self
        else:
            this = self.get_swapped_copy()
        ans = this.get_hash().replace(" ", "-")
        return "{}'s turn:\n{}\n{}\n{}".format(["O", "X"][self.active_player], ans[0:3], ans[3:6], ans[6:9])
        
if __name__ == "__main__":
    import random
    t = TicTacToe()
    while t.who_won() is None:
        print(t.state)
        print("'"+t.get_hash()+"'")
        t.make_move(random.choice(t.get_possible_moves()))
    print(t.state)
    print("'"+t.get_hash()+"'")
    print(t.who_won())
    print(t)
    t.swap_players()
    print(t)