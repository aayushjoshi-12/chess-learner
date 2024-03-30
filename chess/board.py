from collections import namedtuple
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)

Coordinates = namedtuple("Coordinates", ["rank", "file"])

class Board:
    position = []

    def __init__(self, black_player, white_player):
        Board.position = [[None] * 8 for _ in range(8)]

        for player in (black_player, white_player):
            for piece in player.pieces:
                rank, file = piece.coordinates
                self.position[rank][file] = piece

    def display(self):
        for rank in self.position:
            for piece in rank:
                if piece is None:
                    print("0", end="")
                else:
                    print(piece.icon, end="")
            print()

def square_name(coordinates):
    return f"{chr(coordinates.file + 97)}{coordinates.rank + 1}"
            
def square_exists(coordinates):
    rank, file = coordinates
    return (rank >= 0 and rank < 8) and (file >= 0 and file < 8)

def square_empty(coordinates, board=None):
    if board is None: board = Board.position
    return board[coordinates.rank][coordinates.file] == None

def not_friendly_fire(piece, coordinates, board=None):
    if board is None: board = Board.position
    return board[coordinates.rank][coordinates.file].is_white ^ piece.is_white

def calculate_diagonal_moves(piece):
    all_possible_moves = []
    position = piece.coordinates
    all_directions = [
        Direction.UP_LEFT,
        Direction.UP_RIGHT,
        Direction.DOWN_LEFT,
        Direction.DOWN_RIGHT,
    ]
    for direction in all_directions:
        new_coordinate = Coordinates(*tuple(p + d for p, d in zip((position.rank, position.file), direction.value)))    
        while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
            all_possible_moves += [new_coordinate]
            new_coordinate = Coordinates(*tuple(p + d for p, d in zip((new_coordinate.rank, new_coordinate.file), direction.value)))

    return all_possible_moves

def calculate_straight_moves(piece):
    all_possible_moves = []
    position = piece.coordinates
    all_directions = [
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
    ]
    for direction in all_directions:
        new_coordinate = Coordinates(*tuple(p + d for p, d in zip((position.rank, position.file), direction.value)))    
        while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
            all_possible_moves += [new_coordinate]
            new_coordinate = Coordinates(*tuple(p + d for p, d in zip((new_coordinate.rank, new_coordinate.file), direction.value)))
            
    return all_possible_moves

def move_name(piece_name, initial, final):
    # use + , x , # , 0-0 , 0-0-0 , = for check, capture, mate, shortcastle, longcastle, promotion
    # it is for vanity we'll deal with this later
    pass