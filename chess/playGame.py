from player import Player, make_move
from board import Board
from pieces import *

white = Player(is_white=True)
black = Player(is_white=False)
board = Board(black, white)

running = True
whites_turn = True
check_mate = False
board.display()

if __name__ == "__main__":
    while running:
        make_move(white, black)
        board.display()
        make_move(black, white)
        board.display()

### Fools Mate 11 10 13 21