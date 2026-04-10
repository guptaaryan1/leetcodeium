class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = set()
        colset = set()
        boxset = set()
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if ((board[row][col] not in rowset) and board[row][col].isdigit()):
                    rowset.add(board[row][col])
                elif (board[row][col] in rowset):
                    print("row")
                    return False
            rowset.clear()
        for col in range(cols):
            for row in range(rows):
                if ((board[row][col] not in colset) and board[row][col].isdigit()):
                    colset.add(board[row][col])
                elif (board[row][col] in colset):
                    print("col")
                    return False
            colset.clear()
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                for rr in range(row, row + 3):
                    for cc in range(col, col + 3):
                        if ((board[rr][cc] not in boxset) and board[rr][cc].isdigit()):
                            boxset.add(board[rr][cc])
                        elif (board[rr][cc] in boxset):
                            print("box")
                            return False
                boxset.clear()
        return True

            
                

        