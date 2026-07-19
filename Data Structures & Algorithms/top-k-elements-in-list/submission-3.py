class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        pairs = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [pairs[i][0] for i in range(k)]
        
