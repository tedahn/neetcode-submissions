class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) memory
        # find water trapped in every single index
        # an array of water trapped per index
        # max left height array
        # max right height array
        # minimmum between two max height arrays
        # determine water trapped per index (min(l,r) - h[i])
        # O(1) memory optimization
        # start with L and R two pointer from furthest left and right
        # track the maximum height seen from the left and right
        # shift the pointer with the smaller maximum height
        #
        # if the left maximum is smaller, the left side is the limiting boundary,
        # so move L inward and calculate the water trapped at that index using:
        # left_max - height[L]
        # otherwise, the right maximum is the limiting boundary,
        # so move R inward and calculate the water trapped at that index using:
        # right_max - height[R]
        #
        # because we always process the side with the smaller maximum height,
        # we know the opposite side has a boundary that is at least as tall.
        # This means the water can be calculated accurately for the pointer
        # that is being moved.
        # continue until the pointers cross
        # at the end, return the total amount of trapped water
        if not height: return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res
        