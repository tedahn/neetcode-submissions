class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack pair index** height
        # for heights
        # calculate max area as you fill stack with earliest eligible index of the height
        # reverse pop remaining stack and compare to max area
        # return max area
        # t O(n) m O(n)
        maxArea = 0
        stack = [] # list of index, height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea,height*(i-index))
                start = index
            stack.append([start,h])

        for index, height in stack:
            maxArea = max(maxArea,height * (len(heights)-index))
        
        return maxArea