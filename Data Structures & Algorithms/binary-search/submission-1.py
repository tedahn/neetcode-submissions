class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # write a sorting algorithm in O(log n) - binary search
        # common question variation. need to memorize
        # divide the length by half and check the value in the middle to the target.
        # if smaller/larger divide by half and take the other half including the target's range
        # continue to divide and check until you find the value.
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2 
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1