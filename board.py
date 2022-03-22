import piece

class Board():
    """A board class to initialize board and store pieces

    A 8 x 8 grid to record the current game info

    Attributes:
        _board: a 8 x 8 grid indicating the board info. 
    """
    def __init__(self):
        # initialize board
        self.board = [[None] * 8 for _ in range(8)]
        
        # White
        self.board[0][0] = piece.Rook(True)
        self.board[0][1] = piece.Knight(True)
        self.board[0][2] = piece.Bishop(True)
        self.board[0][3] = piece.Queen(True)
        self.board[0][4] = piece.King(True)
        self.board[0][5] = piece.Bishop(True)
        self.board[0][6] = piece.Knight(True)
        self.board[0][7] = piece.Rook(True)

        # Black
        self.board[7][0] = piece.Rook(False)
        self.board[7][1] = piece.Knight(False)
        self.board[7][2] = piece.Bishop(False)
        self.board[7][3] = piece.Queen(False)
        self.board[7][4] = piece.King(False)
        self.board[7][5] = piece.Bishop(False)
        self.board[7][6] = piece.Knight(False)
        self.board[7][7] = piece.Rook(False)

        # Pawns
        for i in range(8):
            self.board[1][i] = piece.Pawn(True)
            self.board[6][i] = piece.Pawn(False)
    

    def print(self) -> str:
        """
        Print current board game
        """
        board_str = " ------------------------\n"
        for i in range(len(self.board)-1, -1, -1):
            board_str += str(i+1) + "|"
            for j in range(len(self.board[i])):
                curr_position = self.board[i][j]
                board_str += str(curr_position) if curr_position else "  " 
                board_str += "|"
            board_str += "\n"
        board_str += " ------------------------\n"
        board_str += "  a  b  c  d  e  f  g  h"
        print(board_str)
