class Piece():
    isWhite : bool = None
    value : int = None
    position : tuple = None

    def __init__(self, isWhite, value):
        Piece.isWhite = isWhite
        Piece.value = value
        Piece.position = (0, None) if isWhite else (7, None)

class King(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, None)

class Queen(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 9)

class Rook(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 5)

class Bishop(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 3)

class Knight(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 3)

class Pawn(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 1)
