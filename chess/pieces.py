from board import square_exists, square_empty, not_friendly_fire, calculate_straight_moves, calulate_diagonal_moves

class King:
    def __init__(self, is_white):
        self.is_white = is_white
        self.coordinates = [7, 3] if is_white else [0, 4]
        self.name = "K" if is_white else "k"
    
    def all_possible_moves(self):
        all_directions = [
            # moves in all f*cking directions and still useless
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
        self.coordinates = [7,4] if is_white else [0,3]
        self.name = "Q" if is_white else "q"

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
        self.coordinates = [7 if is_white else 0, 0 if Rook.no_of_pieces == 1 else 7]
        self.name = "R" if is_white else "r"

    def all_possible_moves(self):
        all_possible_moves = calculate_straight_moves(self)
        return all_possible_moves


class Bishop:
    no_of_pieces = 0

    def __init__(self, is_white):
        Bishop.no_of_pieces += 1
        if Bishop.no_of_pieces > 2 :
            Bishop.no_of_pieces = 1
        self.is_white = is_white
        self.value = 3
        self.coordinates = [7 if is_white else 0, 2 if Bishop.no_of_pieces == 1 else 5]
        self.name = "B" if is_white else "b"

    def all_possible_moves(self):
        all_possible_moves = calulate_diagonal_moves(self)
        return all_possible_moves


class Knight:
    no_of_pieces = 0

    def __init__(self, is_white):
        Knight.no_of_pieces += 1
        if Knight.no_of_pieces > 2 :
            Knight.no_of_pieces = 1
        self.is_white = is_white
        self.value = 3
        self.coordinates = [7 if is_white else 0, 1 if Knight.no_of_pieces == 1 else 6]
        self.name = "N" if is_white else "n"

    def all_possible_moves(self):

        pass


class Pawn:
    no_of_pieces = 0

    def __init__(self, is_white):
        Pawn.no_of_pieces += 1
        if Pawn.no_of_pieces > 8:
            Pawn.no_of_pieces = 1
        self.is_white = is_white
        self.value = 1
        self.coordinates = (6 if is_white else 1, Pawn.no_of_pieces-1)
        self.name = "P" if is_white else "p"
        self.first_move = True

    def all_possible_moves(self):
        # en passant is still remaining
        all_possible_moves = []        

        if self.first_move :
            # if first move two options to move 1 or 2 steps
            new_coordinate = [self.coordinates[0] - 1 if self.is_white else self.coordinates[0] + 1, self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]
            new_coordinate = [self.coordinates[0] - 2 if self.is_white else self.coordinates[0] + 2, self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(self, new_coordinate):
                all_possible_moves += [new_coordinate]
            self.first_move = False
        else :
            # if not first move moves only a single step
            new_coordinate = [self.coordinates[0] - 1 if self.is_white else self.coordinates[0] + 1 , self.coordinates[1]]
            if square_exists(new_coordinate) or not_friendly_fire(new_coordinate):
                all_possible_moves += [new_coordinate]

        # moves to capture diagonally
        new_coordinate = [self.coordinates[0] - 1 if self.is_white else self.coordinates[0] + 1, self.coordinates[1] - 1]
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]
        new_coordinate = [self.coordinates[0] - 1 if self.is_white else self.coordinates[0] + 1, self.coordinates[1] + 1]
        if square_exists(new_coordinate) and not square_empty(new_coordinate) and not_friendly_fire(self, new_coordinate):
            all_possible_moves += [new_coordinate]

        return all_possible_moves