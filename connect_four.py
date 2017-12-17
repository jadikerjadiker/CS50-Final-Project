from game import Game
from sizeable_connect_x import SizeableConnectX


class ConnectFour(SizeableConnectX):
    def __init__(self):
        '''Initialize a connect4 game with 6 rows and 7 columns'''
        super().__init__(6, 7, 4)


if __name__ == "__main__":
    from players import RandomPlayer
    print("Getting random game!")
    c = RandomPlayer.get_random_game(ConnectFour)
    print(c)
    print(c.who_won())
    c.swap_players()
    print(c)

    # haha this takes forever. 64! is under a googol, but not by too much, so that's expected
    print(ConnectFour().get_complexity(-1))