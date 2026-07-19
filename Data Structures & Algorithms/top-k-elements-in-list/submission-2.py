class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        heap = [(-c, n) for n, c in count.items()]
        heapq.heapify(heap)   # O(n)
        return [heapq.heappop(heap)[1] for _ in range(k)]