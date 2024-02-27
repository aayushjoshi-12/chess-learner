from pieces import *

class Player:
    isWhite : bool = None

    def __init__(self, isWhite):
        rook1 = Rook(isWhite)
        knight1 = Knight(isWhite)
        bishop1 = Bishop(isWhite)
        queen = Queen(isWhite)
        king = King(isWhite)
        bishop2 = Bishop(isWhite)
        knight2 = Knight(isWhite)
        rook2 = Rook(isWhite)
        pawn1 = Pawn(isWhite)
        pawn2 = Pawn(isWhite)
        pawn3 = Pawn(isWhite)
        pawn4 = Pawn(isWhite)
        pawn5 = Pawn(isWhite)
        pawn6 = Pawn(isWhite)
        pawn7 = Pawn(isWhite)
        pawn8 = Pawn(isWhite)

    def make_move():
        pass

white = Player(isWhite=True)
black = Player(isWhite=False)
