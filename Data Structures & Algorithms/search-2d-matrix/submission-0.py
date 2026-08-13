class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sorted rows but mixed
        # O (mlogn)
        # sorted and row is greater than the last row
        # O(logm + logn) 
        # 
        # search middle of matrix
        # compare L and R with target. 
        # if in range continue binary searching the row 
        # if not continue to move to a different row by searching middle using col L+R // 2
        # then return true when output is found
        # return false if while loop exits with none found.

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
            
        