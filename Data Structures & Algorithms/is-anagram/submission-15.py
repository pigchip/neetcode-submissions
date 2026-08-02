class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a = []
        b = []

        for i in enumerate(s):
            print(i)
            a.append(s[i])
            b.append(t[i])

        sorted(a)
        sorted(b)   

        print(a,b)

        if a == b:
            return True
        else:
            return False