class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # because it's sorted matrix you can treat it as one single array
        # without even creating a new array
        ROWS, COLS = len(matrix), len(matrix[0])

        # everything else is the basic binsrch
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            mid = (left + right) // 2

            # this is the traversal technique that treats this as 1D arr
            row = mid // COLS
            col = mid % COLS

            value = matrix[row][col]
            # eof
            
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False