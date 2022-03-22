# Pawn_Chess_Game
Implement a pawn chess game in python

## Board
Board: 8 x 8 grid

Rows: a, b, c, d, e, f, g, h

Cols: 1, 2, 3, 4, 5, 6, 7, 8

Pieces: King, Queen, Rook, Bishop, Knight, Pawn 

Opposite: White and Black

```
 ------------------------
8|BR|BN|BB|BQ|BK|BB|BN|BR|
7|BP|BP|BP|BP|BP|BP|BP|BP|
6|  |  |  |  |  |  |  |  |
5|  |  |  |  |  |  |  |  |
4|  |  |  |  |  |  |  |  |
3|  |  |  |  |  |  |  |  |
2|WP|WP|WP|WP|WP|WP|WP|WP|
1|WR|WN|WB|WQ|WK|WB|WN|WR|
 ------------------------
  a  b  c  d  e  f  g  h
```

## Piece Rules
King: Color, str, 
Move: 
1. 8 directions 1 step and 
2. never move to the places to be checked)

Castle:
1. king's first move
2. rook's first move
3. no piece between them
4. king may not be checked or pass through check
5. steps: Rook moves to the side of king and king go the another side of rook

Queen: Color, str, 
Move:
1. 8 direction multiple steps
2. stop when capture opposite piece or meet own side piece

Rook: Color, str,
Move:
1. 4 direction multiple steps
2. stop when capture opposite piece or meet own side piece

Bishop: Color, str, 
Move:
1. diagonally direction
2. stop when capture opposite piece or meet own side piece

Knight: Color, str,
Move:
1. L shape with one more 90 degree 1 step

Pawn: Color, str, first_move, promotion
Move:
1. first_move: one or two steps
2. one step, diagonal eat
3. "en passant", if go two steps firstly, the opposite pawn in the same line can jump diagonally to eat it in next run.