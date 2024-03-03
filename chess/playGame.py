from player import Player
from board import Board
from pieces import *

white = Player(is_white=True)
black = Player(is_white=False)
board = Board(black, white)

running = True

while running:
    board.display()
    for piece in black.pieces:
        if not isinstance(piece, Knight) :
            print(piece.all_possible_moves())
    running = False
