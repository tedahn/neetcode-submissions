class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Linear time solution: O(n)
        # left pointer, right pointer, left most and right most
        # max area
        # shift smaller, left or right.
        # update max area
        # shift smaller, left or right
        # ...
        # left or right are equal to each other shift either left or right, doesn't matter (why?)
        # ...
        # stop when left and right crash into each other
        # reutrn max area
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height

            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area