class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a = []
        b = []

        for i in enumerate(s):
            a.append(s[i[0]])
            b.append(t[i[0]])

        sorted(a)
        sorted(b)   

        print(a,b)

        if a == b:
            return True
        else:
            return False