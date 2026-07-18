class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen={}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for ch in t:
            if ch in seen and seen[ch] > 0:
                seen[ch] -= 1
            else:
                return False

        return True

