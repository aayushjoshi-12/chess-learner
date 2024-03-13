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

    def make_move(self):
        # implement capture logic as well
        all_possible_moves = {}
        i = 0
        for piece in self.pieces:
            for move in piece.all_possible_moves():
                new_position = Board.position.copy()
                new_position[move[0]][move[1]] = piece
                new_position[piece.coordinates[0]][piece.coordinates[1]] = None
                if no_check(self, new_position):
                    all_possible_moves[i] = move
                    print(f"Press {i} to move {piece.name} from {square_name(piece.coordinates)} to {square_name(move)}")
        #----#
        # her we will implement the neural networks result
        #----#
        num = input()
        Board.position[move[0]][move[1]] = piece
        Board.position[piece.coordinates[0]][piece.coordinates[1]] = None
                    

def no_check(player, new_position):
    # first you would technically need to move the piece to figure it out
    # also check while castling
    position = player.king.coordinates
    check_squares_for_knights = [
        [position[0] + 2, position[1] - 1],
        [position[0] + 2, position[1] + 1],
        [position[0] - 2, position[1] - 1],
        [position[0] - 2, position[1] + 1],
        [position[0] - 1, position[1] + 2],
        [position[0] + 1, position[1] + 2],
        [position[0] - 1, position[1] - 2],
        [position[0] + 1, position[1] - 2],
    ]
    for square in check_squares_for_knights:
        if isinstance(new_position[position[0][position[1]]], Knight) and not_friendly_fire(player, square, new_position): 
            # here the function requires piece to find color but we can use player for that purpose as well
            return False
    check_squares_for_pawns = [
        [position[0] - 1 if player.is_white else position[0] + 1, position[1] - 1]
        [position[0] - 1 if player.is_white else position[0] + 1, position[1] + 1]
    ]
    for square in check_squares_for_pawns:
        if isinstance(new_position[position[0][position[1]]], Pawn) and not_friendly_fire(player, square, new_position):
            return False
    check_straight_directions = [
        [position[0] + 1, position[1]    ],
        [position[0]    , position[1] + 1],
        [position[0] - 1, position[1]    ],
        [position[0]    , position[1] - 1],
    ]
    for new_coordinate in check_straight_directions:
        while square_exists(new_coordinate) and (square_empty(new_coordinate, new_position) or not_friendly_fire(player, new_coordinate, new_position)):
            all_possible_moves += [new_coordinate]
            if not_friendly_fire(player, new_coordinate): return False
            new_coordinate[0] += 1
    check_diagonal_directions = [
        [position[0] + 1, position[1] - 1],
        [position[0] + 1, position[1] + 1],
        [position[0] - 1, position[1] + 1],
        [position[0] - 1, position[1] - 1],
    ]
    for new_coordinate in check_diagonal_directions:
        while square_exists(new_coordinate) and (square_empty(new_coordinate, new_position) or not_friendly_fire(player, new_coordinate, new_position)):
            all_possible_moves += [new_coordinate]
            if not_friendly_fire(player, new_coordinate): return False
            new_coordinate[0] += 1
            new_coordinate[1] -= 1

    return True
        
# we can create a custom data structure which would hold things like 
# move increment in value and if it captured something and 
# is it even possible to make the move in case you have a check

# custom data structutre 
# newcoordinate
# new position
# inc in material
# check or not or mate