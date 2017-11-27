'''
By London Lowmanstone
Class for the game Tic-tac-toe
'''

from Game import Game

class TicTacToe(Game):
    '''
    TODO documentation
    '''
    def get_initial_state(self):
        # return an empty board and player #0
        return ([-1] * 9, 0)
    
    def get_properties(self):
        return self.state
    
    def get_copy(self):
        return TicTacToe((self.state[:], self.active_player))
    
    def get_hash(self):
        string_list = ["O", "X", " "]
        ans = ["O", "X"][self.active_player]
        for val in self.state:
            ans += string_list[val]
        return ans
    
    def get_possible_actions(self):
        return [i for i in range(len(self.state)) if self.state[i] == -1]
        
    def make_move(self, action):
        self.state[action] = self.active_player
        self.active_player = Game.other_player(self.active_player)
        
    def who_won(self):
        '''returns 0 if player 0 won, 1 if player 1 won, -1 if it's a tie and None if it's unfinished'''
        if -1 in self.state: #game is not done, default to unfinished
            ans = None
        else: #game is done, default to tie
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
                if checking < 2: #checking rows and columns
                    for j in range(3):
                        if checking == 0: #checking rows
                            # iterate through the row
                            val = self.state[i * 3 + j]
                        else: #checking columns
                            # iterate through the column
                            val = self.state[i + j * 3]
                        
                        if val == -1: # person doesn't have the entire row or column
                            break
                        else:
                            if j == 0: #if it just started checking this line
                                # whoever has the first space must have the other two to win
                                player = val
                            elif not val == player: #if the player doesn't have a win
                                break
                            elif j==2:
                                # if the player does have a win
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
        ans = self.get_hash().replace(" ", "-")
        return "{}'s turn:\n{}\n{}\n{}".format(ans[:1], ans[1:4], ans[4:7], ans[7:10])
        
if __name__ == "__main__":
    import random
    t = TicTacToe()
    while t.who_won() is None:
        print(t.state)
        print("'"+t.get_hash()+"'")
        t.make_move(random.choice(t.get_possible_actions()))
    print(t.state)
    print("'"+t.get_hash()+"'")
    print(t.who_won())
    print(t)