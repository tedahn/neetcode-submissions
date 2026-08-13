import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I need to detect duplicates in every row, column, and 3x3 square.
        # I'll use sets because they let me check whether I've seen a digit
        # before in constant average time.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        # For the squares, I'll use (row // 3, col // 3) as the key.
        # Integer division groups indexes 0-2, 3-5, and 6-8 together,
        # so every cell in the same 3x3 square gets the same key.
        squares = collections.defaultdict(set)

        # Now I'll scan the board one cell at a time.
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                # A dot is an empty cell, so there's nothing to validate here.
                if value == ".":
                    continue

                # This tells me which of the nine 3x3 squares I'm currently in.
                square = (r // 3, c // 3)

                # Before adding this digit, I'll check all three Sudoku rules.
                # If it already exists in any corresponding set, I found a
                # duplicate and can return False immediately.
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[square]
                ):
                    return False

                # Otherwise, this digit is valid so far. I'll record it in its
                # row, column, and square for the cells I process later.
                rows[r].add(value)
                cols[c].add(value)
                squares[square].add(value)

        # If I make it through the entire board, I never found a duplicate,
        # so the current Sudoku board is valid.
        return True