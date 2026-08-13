class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted array is the hint that binary search will work here
        # start by finding the middle l + r // 2
        # compare middle to left and then right
        # find the smaller array
        # if m >= l
        # new L = m + 1
        # else if m >= r
        # new R = m - 1
        # find new m find smaller array again
        # result is updated to m
        # once L and R cross the search ends
        # return result
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                # Minimum is to the right of m
                l = m + 1
            else:
                # Minimum may be at m or to the left
                r = m - 1

        return res
