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
    rank, file = coordinates
    return f"{chr(file + 97)}{rank}"
            
def square_exists(coordinates):
    rank, file = coordinates
    return (rank >= 0 and rank < 8) and (file >= 0 and file < 8)

def square_empty(coordinates, position = Board.position):
    rank, file = coordinates
    return position[rank][file] == None

def not_friendly_fire(piece, coordinates, position = Board.position):
    rank, file = coordinates
    return position[rank][file].is_white ^ piece.is_white

def calulate_diagonal_moves(piece):
    # try simplifying it later and make it a bit less hardcoded if it is even possible
    all_possible_moves = []
    new_coordinate = [piece.coordinates[0] + 1, piece.coordinates[1] + 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] += 1
        new_coordinate[1] += 1
    new_coordinate = [piece.coordinates[0] - 1, piece.coordinates[1] + 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] -= 1
        new_coordinate[1] += 1
    new_coordinate = [piece.coordinates[0] - 1, piece.coordinates[1] - 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] -= 1
        new_coordinate[1] += 1
    new_coordinate = [piece.coordinates[0] + 1, piece.coordinates[1] - 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] += 1
        new_coordinate[1] -= 1

    return all_possible_moves

def calculate_straight_moves(piece):
    all_possible_moves = []
    new_coordinate = [piece.coordinates[0] + 1, piece.coordinates[1]]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] += 1
    new_coordinate = [piece.coordinates[0] - 1, piece.coordinates[1]]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[0] -= 1
    new_coordinate = [piece.coordinates[0], piece.coordinates[1] + 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[1] += 1
    new_coordinate = [piece.coordinates[0], piece.coordinates[1] - 1]
    while square_exists(new_coordinate) and (square_empty(new_coordinate) or not_friendly_fire(piece, new_coordinate)):
        all_possible_moves += [new_coordinate]
        if not_friendly_fire(piece, new_coordinate): break
        new_coordinate[1] -= 1
    
    return all_possible_moves

def move_name(piece_name, from_, to):
    # use + , x , # , 0-0 , 0-0-0 , = for check, capture, mate, shortcastle, longcastle, promotion
    # it is for vanity we'll deal with this later
    pass