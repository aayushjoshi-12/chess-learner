from collections import namedtuple
from board import Board, Direction, square_exists, square_empty, square_name, not_friendly_fire, calculate_straight_moves, calculate_diagonal_moves

Coordinates = namedtuple("Coordinates", ["rank", "file"])

class King:
    def __init__(self, is_white):
        self.is_white = is_white
        self.coordinates = Coordinates(0, 4) if is_white else Coordinates(7, 4)
        self.icon = "K" if is_white else "k"
        self.name = "King"
    
    def all_possible_moves(self):
        all_directions = [
            # castling remaining
            Coordinates(self.coordinates.rank + 1, self.coordinates.file - 1),
            Coordinates(self.coordinates.rank + 1, self.coordinates.file    ),
            Coordinates(self.coordinates.rank + 1, self.coordinates.file + 1),
            Coordinates(self.coordinates.rank    , self.coordinates.file + 1),
            Coordinates(self.coordinates.rank - 1, self.coordinates.file + 1),
            Coordinates(self.coordinates.rank - 1, self.coordinates.file    ),
            Coordinates(self.coordinates.rank - 1, self.coordinates.file - 1),
            Coordinates(self.coordinates.rank    , self.coordinates.file - 1),
        ]
        all_possible_moves = []
        for new_coordinate in all_directions:
            if square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(self, new_coordinate)):
                all_possible_moves += [new_coordinate]
        
        return all_possible_moves


class Queen:
    def __init__(self, is_white):
        self.is_white = is_white
        self.value = 9
        self.coordinates = Coordinates(0, 3) if is_white else Coordinates(7, 3)
        self.icon = "Q" if is_white else "q"
        self.name = "Queen"

    def all_possible_moves(self):
        all_possible_moves = []
        all_possible_moves += calculate_diagonal_moves(self)
        all_possible_moves += calculate_straight_moves(self)
        
        return all_possible_moves


class Rook:
    no_of_pieces = 0

    def __init__(self, is_white):
        Rook.no_of_pieces += 1
        if Rook.no_of_pieces > 2 :
            Rook.no_of_pieces = 1
        self.is_white = is_white
        self.value = 5
        self.coordinates = Coordinates(0 if is_white else 7, 0 if Rook.no_of_pieces == 1 else 7)
        self.icon = "R" if is_white else "r"
        self.name = "Rook"

    def all_possible_moves(self):
        return calculate_straight_moves(self)


class Bishop:
    no_of_pieces = 0

    def __init__(self, is_white):
        Bishop.no_of_pieces += 1
        if Bishop.no_of_pieces > 2 :
            Bishop.no_of_pieces = 1
        self.is_white = is_white
        self.value = 3
        self.coordinates = Coordinates(0 if is_white else 7, 2 if Bishop.no_of_pieces == 1 else 5)
        self.icon = "B" if is_white else "b"
        self.name = "Bishop"

    def all_possible_moves(self):
        return calculate_diagonal_moves(self)


class Knight:
    no_of_pieces = 0

    def __init__(self, is_white):
        Knight.no_of_pieces += 1
        if Knight.no_of_pieces > 2 :
            Knight.no_of_pieces = 1
        self.is_white = is_white
        self.value = 3
        self.coordinates = Coordinates(0 if is_white else 7, 1 if Knight.no_of_pieces == 1 else 6)
        self.icon = "N" if is_white else "n"
        self.name = "Knight"

    def all_possible_moves(self):
        all_possible_moves = []
        all_directions = [
            Coordinates(self.coordinates.rank + 2, self.coordinates.file - 1),
            Coordinates(self.coordinates.rank + 2, self.coordinates.file + 1),
            Coordinates(self.coordinates.rank - 2, self.coordinates.file - 1),
            Coordinates(self.coordinates.rank - 2, self.coordinates.file + 1),
            Coordinates(self.coordinates.rank - 1, self.coordinates.file + 2),
            Coordinates(self.coordinates.rank + 1, self.coordinates.file + 2),
            Coordinates(self.coordinates.rank - 1, self.coordinates.file - 2),
            Coordinates(self.coordinates.rank + 1, self.coordinates.file - 2),
        ]
        for coordinate in all_directions:
            if square_exists(coordinate) and (square_empty(coordinate) or not_friendly_fire(self, coordinate)):
                all_possible_moves += [coordinate]

        return all_possible_moves


class Pawn:
    no_of_pieces = 0

    def __init__(self, is_white):
        Pawn.no_of_pieces += 1
        if Pawn.no_of_pieces > 8:
            Pawn.no_of_pieces = 1
        self.is_white = is_white
        self.first_move = True
        self.value = 1
        self.coordinates = Coordinates(1 if is_white else 6, Pawn.no_of_pieces-1)
        self.icon = "P" if is_white else "p"
        self.name = "Pawn"

    def all_possible_moves(self):
        # en passant is still remaining
        all_possible_moves = []

        if self.first_move :
            new_coordinate = Coordinates(self.coordinates.rank + 1 if self.is_white else self.coordinates.rank - 1, self.coordinates.file)
            if square_exists(new_coordinate) and square_empty(new_coordinate):
                all_possible_moves += [new_coordinate]
            new_coordinate = Coordinates(self.coordinates.rank + 2 if self.is_white else self.coordinates.rank - 2, self.coordinates.file)
            if square_exists(new_coordinate) and square_empty(new_coordinate):
                all_possible_moves += [new_coordinate]
        else :
            new_coordinate = Coordinates(self.coordinates.rank + 1 if self.is_white else self.coordinates.rank - 1 , self.coordinates.file)
            if square_exists(new_coordinate) and square_empty(new_coordinate):
                all_possible_moves += [new_coordinate]
        
        new_coordinate = Coordinates(self.coordinates.rank + 1 if self.is_white else self.coordinates.rank - 1, self.coordinates.file - 1)
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]
        new_coordinate = Coordinates(self.coordinates.rank + 1 if self.is_white else self.coordinates.rank - 1, self.coordinates.file + 1)
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]

        return all_possible_moves