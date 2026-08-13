class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force, slowest to fastest eating until answer is found O(max(p))
        # binsrch optimization, O(log(max(p)))
        # k array of possible answers. L = min , R = max. binary search the k array per koko's eating speed.
        # get the hours taken to eat all the pile with k speed.
        # the hour is lower than h. so it's potentially the answer.
        # if the hour is higher than h then move new k + 1
        # but search again in the smaller k value
        # new R = k - 1
        # new k = l + r // 2
        # try the new speed and get the time taken.
        # if new K works then replace the results
        # when R crosses L, the search ends
        # return the result

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles: 
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            
