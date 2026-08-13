class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing brackets to their corresponding opening brackets
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in pair:  # it's a closing bracket
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
            else:  # it's an opening bracket
                stack.append(char)

        # Stack should be empty if all brackets are properly closed
        return not stack