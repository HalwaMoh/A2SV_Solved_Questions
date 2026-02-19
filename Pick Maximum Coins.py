class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        n=len(piles)//3
        res=0
        for i in range(1,n*2,2):
            res+=piles[i]
        return res    



        
        
