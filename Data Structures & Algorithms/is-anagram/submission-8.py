class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = s.split()
        b = t.split()

        sorted(a)

        sorted(b)
        print(a,b)

        if a == b:
            return True
        else:
            return False