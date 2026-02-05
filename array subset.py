class Solution:
   def isSubset(self, a, b):
        cntA=counter(a)
        cntB=counter(b)
        for x in range(cntB):
            if cntB[x] > cntA.get(x, 0):
                return False

        return True
