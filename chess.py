import board
import piece

class Chess():
    """A class to start chess game

    To initialize chess game and operation
    """
    def __init__(self):
        self._boardObject = board.Board()

        self._turn = True
    
    def promotion(self, pos: tuple, color: bool) -> None:
        promp_piece = None
        while not promp_piece:
            promote = input("Promote pawn to [Q, R, N, B, P(or nothing)]: ")
            if promote not in ['Q', 'R', 'N', 'B', 'P', '']:
                print("Not a valid promotion piece")
            else:
                if promote == 'Q':
                    promp_piece = piece.Queen(color)
                elif promote == 'R':
                    promp_piece = piece.Rook(color)
                elif promote == 'N':
                    promp_piece = piece.Knight(color)
                elif promote == 'B':
                    promp_piece = piece.Bishop(color)
                elif promote == 'P' or promote == '': 
                    promp_piece = piece.Pawn(color)
        self._boardObject.board[pos[0]][pos[1]] = promp_piece
    
    def move(self, start: tuple, end: tuple) -> None:
        start_piece = self._boardObject.board[start[0]][start[1]]

        # invalid place
        if not start_piece:
            print("No piece to move")
            return
        
        # not the same turn
        if self._turn != start_piece._color:
            print("Not your turn")
            return
        
        # same side piece
        end_piece = self._boardObject.board[end[0]][end[1]]

        if end_piece and start_piece._color == end_piece._color:
            print("There is a same side piece in destination")
            return
        
        if start_piece.is_valid_move(self._boardObject.board, start, end):

            if end_piece:
                print(str(end_piece) + "taken.")

            self._boardObject.board[end[0]][end[1]] = start_piece
            self._boardObject.board[start[0]][start[1]] = None

            self._turn = not self._turn
        

def translate(s):
    """
    Translates traditional board coordinates of chess into list indices
    """
    try:
        row = int(s[0])
        col = s[1]
        if row < 1 or row > 8:
            print(s[0] + "is not in the range from 1 - 8")
            return None
        if col < 'a' or col > 'h':
            print(s[1] + "is not in the range from a - h")
            return None
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return (row-1, dict[col])
    except:
        print(s + "is not in the format '[number][letter]'")
        return None

def main():
    chess = Chess()
    chess._boardObject.print()
    while True:
        start = input("From: ")
        end = input("To: ")

        start = translate(start)
        end = translate(end)

        print(start)
        print(end)
        if not start or not end:
            continue
        
        chess.move(start, end)
        chess._boardObject.print()
        

if __name__ == "__main__":
    main()