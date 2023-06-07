from typing import List # For annotations

board_count = 0

def IsBoardOk (chessboard : List, row : int, col : int) :

   # Check if there is a queen 'Q' positioned to the left of column col on the same row.
   for c in range(col) :
       if (chessboard[row][c] == 'Q') :
           return False

   # Check if there is queen 'Q' positioned on the upper left diagonal
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (chessboard[r][c] == 'Q') :
           return False

   # Check if there is queen 'Q' positioned on the lower left diagonal
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)) :
      if (chessboard[r][c] == 'Q') :
          return False

   return True

def DisplayBoard (chessboard : List) :

    for row in chessboard :
        print(row)

def PlaceNQueens (chessboard : List, col : int) :

    # If all the columns have a queen 'Q', a solution has been found.
    global board_count

    if (col >= len(chessboard)) :

        board_count += 1
        print("Board " + str(board_count))
        print("==========================")
        DisplayBoard(chessboard)
        print("==========================\n")

    else :

        # Else try placing the queen on each row of the column and check if the chessboard remains OK.
        for row in range(len(chessboard)) :

            chessboard[row][col] = 'Q'

            if (IsBoardOk(chessboard, row, col) == True) :
                # Chess board was OK, hence try placing the queen 'Q' in the next column.
                PlaceNQueens(chessboard, col + 1)

            chessboard[row][col] = '.'; # As previously placed queen was not valid, restore '.'

def main() :

   chessboard = []
   N = int(input("Enter chessboard size : "))

   for i in range(N) :
       row = ["."] * N
       chessboard.append(row)

   # Start placing the queen 'Q' from the 0'th column.
   PlaceNQueens(chessboard, 0)

if __name__ == "__main__" :
    main()