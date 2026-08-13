class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # reverse order first car, second car, 
        # if the cars collide we remove the second card. then add the third car
        # if the third car also collide, we pop that car
        # the length of the stack tells us how many fleets we have.
        pair = [[p, s] for p, s in zip(position, speed)] # list comprehension python

        stack = [] # another DS to see how many cars are stacked
        for p, s in sorted(zip(position, speed), reverse=True): # reverse sorted order 
            stack.append((target - p) / s)

            # the reverse order determines that the current car doens't collide with the next car
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # collission
                stack.pop()
            
        return len(stack)
