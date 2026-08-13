class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pointer 1,2
        # for num in numbers
        # if 1 ... + x == target return pointer 1,2
        # if 1 +x > target reset pointer 1,2
        # t O(n) mem O(1)
        l, r = 0, len(numbers)-1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if(twoSum > target):
                r -= 1
            elif(twoSum < target):
                l += 1
            else:
                return [l + 1, r + 1]
        return []