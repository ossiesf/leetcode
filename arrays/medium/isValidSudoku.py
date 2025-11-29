# Problem Link: https://leetcode.com/problems/valid-sudoku/
# Submission Link: https://leetcode.com/problems/valid-sudoku/submissions/1842443624/
# Complexity of O(1) but this would scale to O(n^2) if we scale the size of the board
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # We want to traverse each square only once, so we have i for row
        # j for col and we calculate which of the 9 3x3 boxes we are in
        for i in range(9):
            for j in range(9):
                box_id = (i // 3) * 3 + j // 3
                value = board[i][j]
                if value == '.':
                    continue
                
                if value in row[i] or value in col[j] or value in boxes[box_id]:
                    return False
                else:
                    row[i].add(value)
                    col[j].add(value)
                    boxes[box_id].add(value)
        return True
