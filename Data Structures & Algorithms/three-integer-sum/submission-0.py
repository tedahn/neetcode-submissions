class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # three pointers
        # result array
        # for num in nums
        # first number current pointer
        # use pointer l and r two sum + current pointer value
        # if no target is 3sum is found, current pointer ++
        # if target is found append to array
        # return result
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([a,nums[l],nums[r]])
                    # [-2,-2, 0, 0, 2, 2]
                    #  ^      ^        ^
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res
