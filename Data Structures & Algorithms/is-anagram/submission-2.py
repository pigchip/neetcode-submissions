class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s).sort()
        b = list(t).sort()

        if a == b:
            return True
        else:
            return False