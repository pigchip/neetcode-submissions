class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = s.split().sort()
        b = t.split().sort()

        print(a,b)

        if a == b:
            return True
        else:
            return False