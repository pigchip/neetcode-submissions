class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = s.split().sort()
        b = t.split().sort()

        if a == b:
            return True
        else:
            return False