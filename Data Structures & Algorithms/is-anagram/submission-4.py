class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = s.sort()
        b = t.sort()

        if a == b:
            return True
        else:
            return False