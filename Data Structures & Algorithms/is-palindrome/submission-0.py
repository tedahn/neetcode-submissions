class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        # reversed string
        # return clean string == reversed string
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]