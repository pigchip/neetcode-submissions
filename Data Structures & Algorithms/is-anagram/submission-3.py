class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s).sort()
        b = list(t).sort()

        print(a,b)

        if a == b:
            return True
        else:
            return False