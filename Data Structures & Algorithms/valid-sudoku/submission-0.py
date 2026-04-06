from typing import List

class Solution:
    def isValidList(self, items: List[str]) -> bool:
        existing_nums = set()
        for n in items:
            if n == '.':
                continue
            if not (n.isdigit() and 1 <= int(n) <= 9):
                return False
            if n in existing_nums:
                return False
            existing_nums.add(n)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.isValidList(row):
                return False

        # Check each column
        for col in zip(*board):
            if not self.isValidList(col):
                return False

        # Check each 3x3 sub-grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not self.isValidList(sub_grid):
                    return False

        return True
