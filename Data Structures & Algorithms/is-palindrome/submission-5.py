class Solution:
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        # L pointer and R pointer
        l, r = 0, len(s) - 1
        
        while l < r:
            # skip if not alpha numeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # compare L and R return false break
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        # if L and R cross return True
        # t O(n) mem O(1)
        return True 
