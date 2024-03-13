from board import Board, square_exists, square_empty, square_name, not_friendly_fire, calculate_straight_moves, calulate_diagonal_moves

class King:
    def __init__(self, is_white):
        self.is_white = is_white
        self.coordinates = [0, 4] if is_white else [7, 3]
        self.icon = "K" if is_white else "k"
        self.name = "King"
    
    def all_possible_moves(self):
        all_directions = [
            # moves in all f*cking directions and still useless
            # castling remaining
            [self.coordinates[0] + 1, self.coordinates[1] - 1],
            [self.coordinates[0] + 1, self.coordinates[1]    ],
            [self.coordinates[0] + 1, self.coordinates[1] + 1],
            [self.coordinates[0]    , self.coordinates[1] + 1],
            [self.coordinates[0] - 1, self.coordinates[1] + 1],
            [self.coordinates[0] - 1, self.coordinates[1]    ],
            [self.coordinates[0] - 1, self.coordinates[1] - 1],
            [self.coordinates[0]    , self.coordinates[1] - 1],
        ]
        all_possible_moves = []
        for new_coordinate in all_directions:
            if square_exists(new_coordinate) and not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]
        
        return all_possible_moves


class Queen:
    def __init__(self, is_white):
        self.is_white = is_white
        self.value = 9
        self.coordinates = [0,3] if is_white else [7,4]
        self.icon = "Q" if is_white else "q"
        self.name = "Queen"

    def all_possible_moves(self):
        all_possible_moves = []
        all_possible_moves += calulate_diagonal_moves(self)
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
        self.coordinates = [0 if is_white else 7, 0 if Rook.no_of_pieces == 1 else 7]
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
        self.coordinates = [0 if is_white else 7, 2 if Bishop.no_of_pieces == 1 else 5]
        self.icon = "B" if is_white else "b"
        self.name = "Bishop"

    def all_possible_moves(self):
        return calulate_diagonal_moves(self)


class Knight:
    no_of_pieces = 0

    def __init__(self, is_white):
        Knight.no_of_pieces += 1
        if Knight.no_of_pieces > 2 :
            Knight.no_of_pieces = 1
        self.is_white = is_white
        self.value = 3
        self.coordinates = [0 if is_white else 7, 1 if Knight.no_of_pieces == 1 else 6]
        self.icon = "N" if is_white else "n"
        self.name = "Knight"

    def all_possible_moves(self):
        all_possible_moves = []
        all_directions = [
            [self.coordinates[0] + 2, self.coordinates[1] - 1],
            [self.coordinates[0] + 2, self.coordinates[1] + 1],
            [self.coordinates[0] - 2, self.coordinates[1] - 1],
            [self.coordinates[0] - 2, self.coordinates[1] + 1],
            [self.coordinates[0] - 1, self.coordinates[1] + 2],
            [self.coordinates[0] + 1, self.coordinates[1] + 2],
            [self.coordinates[0] - 1, self.coordinates[1] - 2],
            [self.coordinates[0] + 1, self.coordinates[1] - 2],
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
        self.coordinates = [1 if is_white else 6, Pawn.no_of_pieces-1]
        self.icon = "P" if is_white else "p"
        self.name = "Pawn"

    def all_possible_moves(self):
        # en passant is still remaining
        all_possible_moves = []        

        if self.first_move :
            # if first move two options to move 1 or 2 steps
            new_coordinate = [self.coordinates[0] + 1 if self.is_white else self.coordinates[0] - 1, self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]
            new_coordinate = [self.coordinates[0] + 2 if self.is_white else self.coordinates[0] - 2, self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]
            self.first_move = False
        else :
            # if not first move moves only a single step
            new_coordinate = [self.coordinates[0] + 1 if self.is_white else self.coordinates[0] - 1 , self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]

        # moves to capture diagonally
        new_coordinate = [self.coordinates[0] + 1 if self.is_white else self.coordinates[0] - 1, self.coordinates[1] - 1]
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]
        new_coordinate = [self.coordinates[0] + 1 if self.is_white else self.coordinates[0] - 1, self.coordinates[1] + 1]
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]

        return all_possible_moves