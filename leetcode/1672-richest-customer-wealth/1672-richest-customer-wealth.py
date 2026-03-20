class Solution(object):
    def maximumWealth(self, accounts):
        max_=0
        for row in accounts:
            sum_=sum(row)
            max_=max(max_,sum_)
        return max_   
            
        