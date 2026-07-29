class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        c = 0

        for i, num in enumerate(nums):
            seen[num] = i

        for i, num in enumerate(nums):
            c = target - num
            if c in seen:
                return [i, seen[c]]

        return []