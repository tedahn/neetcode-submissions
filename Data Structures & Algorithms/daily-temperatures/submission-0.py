class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # output 
        res = [0] * len(temperatures)
        # stack
        stack = [] # pair: [temp, index]

        # for temp in temps
        for i, t in enumerate(temperatures):
            # if greater than last stacks 
            while stack and t > stack[-1][0]:
                # update output @ index with i - j
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            # else append temp to stack
            stack.append([t,i])
        # fill rest with 0
        # return output
        return res