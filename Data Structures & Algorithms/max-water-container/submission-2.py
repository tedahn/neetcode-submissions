class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Linear time solution: O(n)
        # left pointer, right pointer, left most and right most
        # max area
        # shift smaller, left or right.
        # update max area
        # shift smaller, left or right
        # ...
        # left or right are equal to each other shift either left or right, doesn't matter (why?) - if you move either pointer, the width decreases, the bar you leave behind still has the same height. Any container using that bar has area at most 5 * smaller_width which is less than the current area... so neither of the equal-height bar will produce a better result.
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