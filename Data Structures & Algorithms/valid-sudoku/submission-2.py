import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I'll track the digits already seen in each row, column, and 3x3 box.
        # Set membership gives me an average O(1) duplicate check.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        # Integer division maps every cell to its box coordinates.
        # For example, rows 3-5 and columns 6-8 all map to box (1, 2).
        squares = collections.defaultdict(set)

        # Invariant: before I process a cell, these sets contain exactly the
        # non-empty digits from the cells I have already visited.
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                # Empty cells do not participate in duplicate checks.
                if value == ".":
                    continue

                square = (r // 3, c // 3)

                # If this digit has appeared in any corresponding unit, the
                # board violates at least one Sudoku rule.
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[square]
                ):
                    return False

                # The digit is valid so far, so I record it for later cells.
                rows[r].add(value)
                cols[c].add(value)
                squares[square].add(value)

        # I visit all 81 cells once with average O(1) set operations.
        # Fixed 9x9 board: O(1) time/space. General n x n board: O(n^2).
        # Reaching this point means every non-empty cell preserved the invariant.
        return True
