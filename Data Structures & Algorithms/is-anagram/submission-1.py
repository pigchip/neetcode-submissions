class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list(s).sort()
        list(t).sort()

        if s == t:
            return True
        else:
            return False