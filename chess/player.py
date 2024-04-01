import copy
from pieces import *

Move = namedtuple("Move", ["piece", "initial", "final", "captured_piece"])

class Player:
    def __init__(self, is_white):
        self.score = 0
        self.no_check = True
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


def make_move(player, opponent):
    moves_dict = {}
    i = 0
    for piece in player.pieces:
        for move in piece.all_possible_moves():
            new_position = copy.deepcopy(Board.position)
            move = Move(piece, piece.coordinates, move, Board.position[move.rank][move.file])
            new_position[move.final.rank][move.final.file] = piece
            new_position[move.initial.rank][move.initial.file] = None
            if no_check(player, new_position):
                i += 1
                moves_dict[i] = move
                print(f"Press {i} to move {piece.name} from {square_name(move.initial)} to {square_name(move.final)}")
    if i == 0 and not player.no_check : 
        print("----------GAME OVER-----------")
        print(f"!!!{opponent} WON!!!")
        exit() # here you would actually start a new game but ig that would be integrated in the train or main loop
    elif i == 0 :
        print("----------GAME OVER-----------")
        print("!!!!!!DRAW!!!!!!")
        exit()
    num = int(input("Enter the move number: "))
    move = moves_dict[num]
    Board.position[move.final.rank][move.final.file] = move.piece
    Board.position[move.initial.rank][move.initial.file] = None
    move.piece.coordinates = move.final
    if isinstance(move.piece, Pawn): move.piece.first_move = False
    if move.captured_piece: 
        player.score += move.captured_piece.value
        player.pieces.remove(move.captured_piece)
    opponent.no_check = no_check(opponent, Board.position)


def find_king_position(player, board_position):
    for rank in board_position:
        for piece in rank:
            if isinstance(piece, King) and not piece.is_white ^ player.is_white:
                return piece.coordinates
    return None


def no_check(player, new_position):
    position = find_king_position(player, new_position)

    check_squares_for_knights = [
        Coordinates(position.rank + 2, position.file - 1),
        Coordinates(position.rank + 2, position.file + 1),
        Coordinates(position.rank - 2, position.file - 1),
        Coordinates(position.rank - 2, position.file + 1),
        Coordinates(position.rank - 1, position.file + 2),
        Coordinates(position.rank + 1, position.file + 2),
        Coordinates(position.rank - 1, position.file - 2),
        Coordinates(position.rank + 1, position.file - 2),
    ]
    for square in check_squares_for_knights:
        if square_exists(square) and isinstance(new_position[square.rank][square.file], Knight) and not_friendly_fire(player, square, new_position): 
            # here the function requires piece to find color but we can use player for that purpose as well (change it later so that it requires the color rather than taking player/piece)
            return False

    check_squares_for_pawns = [
        Coordinates(position.rank - 1 if player.is_white else position.rank + 1, position.file - 1),
        Coordinates(position.rank - 1 if player.is_white else position.rank + 1, position.file + 1),
    ]
    for square in check_squares_for_pawns:
        if square_exists(square) and isinstance(new_position[square.rank][square.file], Pawn) and not_friendly_fire(player, square, new_position):
            return False

    check_straight_directions = [
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
    ]
    for direction in check_straight_directions:
        new_coordinate = Coordinates(*tuple(p + d for p, d in zip((position.rank, position.file), direction.value)))
        while square_exists(new_coordinate):
            if square_empty(new_coordinate, new_position):
                new_coordinate = Coordinates(*tuple(p + d for p, d in zip((new_coordinate.rank, new_coordinate.file), direction.value)))
            elif not_friendly_fire(player, new_coordinate, new_position) and isinstance(new_position[new_coordinate[0]][new_coordinate[1]], (Queen, Rook)):
                return False
            else:
                break

    check_diagonal_directions = [
        Direction.UP_LEFT,
        Direction.UP_RIGHT,
        Direction.DOWN_LEFT,
        Direction.DOWN_RIGHT,
    ]
    for direction in check_diagonal_directions:
        new_coordinate = Coordinates(*tuple(p + d for p, d in zip((position.rank, position.file), direction.value)))
        while square_exists(new_coordinate):
            if square_empty(new_coordinate, new_position):
                new_coordinate = Coordinates(*tuple(p + d for p, d in zip((new_coordinate.rank, new_coordinate.file), direction.value)))
            elif not_friendly_fire(player, new_coordinate, new_position) and isinstance(new_position[new_coordinate[0]][new_coordinate[1]], (Queen, Bishop)):
                return False
            else:
                break

    return True