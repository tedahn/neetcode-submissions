class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack 
        stack = []
        # while tokens
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                stack.append(stack.pop() - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b = stack.pop()
                stack.append(int(stack.pop() / b)) # round to zero
            else:
                stack.append(int(c))

        # return stack pop
        return stack.pop()
