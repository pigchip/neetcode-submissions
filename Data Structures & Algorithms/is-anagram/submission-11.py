class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a = []
        b = []

        for i in enumerate(s):
            a.add(s[i])
            b.add(t[i])

        sorted(a)
        sorted(b)   

        print(a,b)

        if a == b:
            return True
        else:
            return False