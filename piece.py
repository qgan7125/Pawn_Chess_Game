"""Piece class file to create piece object

The file contains classes to declare different pawn chess game
objects. And There are some helper functions to achieve special
game rules.

Author: Quan Gan
Date: 03/21/2022

    Usage example:
    pawn = pawn()
    pawn.is_valid_move()
"""

### The static string for error
ILLEGAL_MOVE = "This is a illegal move."
BLOCKED_MOVE = "This move is blocked."

def check_vertical_horizontal(board: list[list], start: tuple, end: tuple) -> bool:
    """A helper function to check if move is legal

    A helper function to check if the path from start to end 
    in vertical or horizontal direction is legal

    Arguments:
        board: a list of list indicating current board
        start: a tuple indicating start location
        end: a tuple indicating end location
    
    Return:
        a boolean: True if the path is legal
    """
    # Vertical
    if start[0] == end[0]:
        lower_y = min(start[1], end[1])
        upper_y = max(start[1], end[1])

        for i in range(lower_y+1, upper_y):
            if board[start[0]][i] != None:
                print(BLOCKED_MOVE)
                return False
    # Horizontal
    else:
        lower_x = min(start[0], end[0])
        upper_x = max(start[0], end[0])
        for i in range(lower_x+1, upper_x):
            if board[i][0] != None:
                print(BLOCKED_MOVE)
                return False
    return True

def check_diagonal(board: list[list], start: tuple, end: tuple) -> bool:
    """A helper function to check if move is legal

    A helper function to check if the path from start to end 
    in diagonal or anti-diagonal direction is legal

    Arguments:
        board: a list of list indicating current board
        start: a tuple indicating start location
        end: a tuple indicating end location
    
    Return:
        a boolean: True if the path is legal
    """
    # Diagonal
    if start[0] - start[1] == end[0] - end[1]:
        lower = start if end[0] > start[0] else end
        upper = end if lower == start else start

        for _ in range(1, abs(upper[0] - lower[0])):
            x = lower[0] + 1
            y = lower[1] + 1
            if board[x][y] != None:
                print(BLOCKED_MOVE)
                return False
    # Anti-diagonal
    elif start[0] + start[1] == end[0] + end[1]:
        lower = start if end[0] < start[0] else end
        upper = end if lower == start else start

        for _ in range(1, abs(upper[0] - lower[0])):
            x = lower[0] - 1
            y = lower[1] + 1
            if board[x][y] != None:
                print(BLOCKED_MOVE)
                return False

    return True

def mahantan_distance(start: tuple, end: tuple) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

class Piece():
    """Abstract class to piece

    The abstract class of piece contains basic function.

    Attributes:
        _name: A string indicating the name of piece
            Pawn -> P
            Rook -> R
            Knight -> N
            Bishop -> B
            Queen -> Q
            King -> K
        _color: A boolean indicating piece side
            True -> White
            False -> Black
    """

    def __init__(self, name: str, color: bool):
        self._name = name
        self._color = color
    

    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        """ Function to check if inputs are legal move

        Arguments:
            board: A grid of current board
            start: A tuple indicating start location
            end: A tuple indicating destination location

        Return:
            Boolean if from start to end location
        """
        return False
    
    def is_white(self):
        """
        Return:
            True if piece is white
        """
        return self._color
    
    def __str__(self):
        """
        Return:
            A string indicating the color and name of piece
            ex. WK for the White King
        """
        return "{0}{1}".format("W" if self._color else "B" ,self._name) 

class Rook(Piece):
    """A class of Rook

    Attributes:
        same attributes with piece
        _first_move: a boolean indicating if it's first move for castle
    """

    def __init__(self, color: bool):
        super().__init__('R', color)
        self._first_move = True

    def is_valid_move(self, board: list[list], start: str, end: str) -> bool:
        if start[0] == end[0] or start[1] == end[1]:
            return check_vertical_horizontal(board, start, end)
        print(ILLEGAL_MOVE)
        return False
    
    def is_first_Move(self):
        return self._first_move
    
    def not_first_Move(self) -> None:
        self._first_move = not self._first_move

class Knight(Piece):
    """A class of Knight

    Attributes:
        same attributes with piece
    """
    def __init__(self, color: bool):
        super().__init__("N", color)
    
    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
            return True

        if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
            return True 
        print(ILLEGAL_MOVE)
        return False

class Bishop(Piece):
    """A class of Bishop

    Attributes:
        same attributes with piece
    """
    def __init__(self, color: bool):
        super().__init__("B", color)
    
    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        if abs(start[0] - start[1]) == abs(end[0] - end[1]) or abs(start[0] + start[1]) == abs(end[0] + end[1]):
            return check_diagonal(board, start, end)
        print(ILLEGAL_MOVE)
        return False

class Queen(Piece):
    """A class of Queen

    Attributes:
        same attributes with piece
    """
    def __init__(self, color: bool):
        super().__init__("Q", color)

    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        # diagonal or anti-diagonal
        if abs(start[0] - start[1]) == abs(end[0] - end[1]) or abs(start[0] + start[1]) == abs(end[0] + end[1]):
            return check_diagonal(board, start, end)
        # Vertical or horizontal
        elif start[0] == end[0] or start[1] == end[1]:
            return check_vertical_horizontal(board, start, end)

        print(ILLEGAL_MOVE)
        return False

class King(Piece):
    """A class of King

    Attributes:
        same attributes with piece
    """
    def __init__(self, color: bool):
        super().__init__("K", color)

    # TODO: castle rule
    # def castle(self, board: list[list], start: tuple, end: tuple, right: bool) => bool:
    
    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        # TODO: castle check


        if mahantan_distance(start, end) <= 2 and mahantan_distance != 0:
            return True
        print(ILLEGAL_MOVE)
        return False

class Pawn(Piece):
    """A class of Pawn

    Attributes:
        same attributes with piece
        _first_move: a boolean if the piece is the first move
    """
    def __init__(self, color: bool):
        super().__init__("P", color)
        self._first_move = True

    def is_valid_move(self, board: list[list], start: tuple, end: tuple) -> bool:
        # TODO en passant

        # if the piece is white, then must move up
        if self._color and start[1] == end[1] and end[0] > start[0] and board[end[0]][end[1]] == None:
            if self._first_move:
                return 0 < end[0] - start[0] <= 2
            else:
                return 0 < end[0] - start[0] <= 1
        # if the piece is black, then must move down
        elif not self._color and start[1] == end[1] and end[0] < start[0] and board[end[0]][end[1]] == None:
            if self._first_move:
                return 0 < start[0] - end[0] <= 2
            else:
                return 0 < start[0] - end[0] <= 1
        print(ILLEGAL_MOVE)
        return False
    
    def is_first_Move(self):
        return self._first_move
    
    def not_first_Move(self) -> None:
        self._first_move = not self._first_move