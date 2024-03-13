from player import Player
from board import Board
from pieces import *

white = Player(is_white=True)
black = Player(is_white=False)
board = Board(black, white)

running = True
whites_turn = True
check_mate = False

while running:
    if whites_turn:
        white.make_move()
    else :
        black.make_move()
        running = False
    
    whites_turn = not whites_turn
    # if check_mate:
    #     running = False

# think for logic for check and check mate and game finish
# think for logic of piece capture