import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowd = collections.defaultdict(set)
        cold = collections.defaultdict(set)
        boxd = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    continue
                if (board[row][col] in rowd[row] or
                    board[row][col] in cold[col] or
                    board[row][col] in boxd[(row//3, col//3)]):
                    return False
                rowd[row].add(board[row][col])
                cold[col].add(board[row][col])
                boxd[(row//3, col//3)].add(board[row][col])
        return True
                    