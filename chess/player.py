from pieces import *

class Player:
    def __init__(self, is_white):
        self.score = 0
        self.is_white = is_white
        self.rook1 = Rook(is_white)
        self.knight1 = Knight(is_white)
        self.bishop1 = Bishop(is_white)
        self.queen = Queen(is_white)
        self.king = King(is_white)
        self.bishop2 = Bishop(is_white)
        self.knight2 = Knight(is_white)
        self.rook2 = Rook(is_white)
        self.pawn1 = Pawn(is_white)
        self.pawn2 = Pawn(is_white)
        self.pawn3 = Pawn(is_white)
        self.pawn4 = Pawn(is_white)
        self.pawn5 = Pawn(is_white)
        self.pawn6 = Pawn(is_white)
        self.pawn7 = Pawn(is_white)
        self.pawn8 = Pawn(is_white)

        self.pieces = [
            self.pawn1, self.pawn2,   self.pawn3,   self.pawn4, self.pawn5, self.pawn6,   self.pawn7,   self.pawn8,
            self.rook1, self.knight1, self.bishop1, self.queen, self.king,  self.bishop2, self.knight2, self.rook2,
        ]

    def all_possible_moves(self):
        for piece in self.pieces:
            for move in piece.all_possible_moves():
                pass