class Solution:
    def isAnagram(self, s: str, t: str):
        sortS=[]
        sortT=[]
        for i in range(len(s)):
            sortS.append(s[i])
        sortS.sort()
        for i in range(len(t)):
            sortT.append(t[i])
        sortT.sort()
        if (sortS == sortT):
            return True
        return False


        