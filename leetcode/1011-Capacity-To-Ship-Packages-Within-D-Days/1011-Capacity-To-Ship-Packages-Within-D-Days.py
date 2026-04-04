class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=max(weights),sum(weights)
        while left<right:
            mid=(left+right)//2
            if self.check(weights,days,mid):
                right=mid
            else:
                left=mid+1
        return left            

    def check(self,weights,days,capacity):
        sum_=0
        day_=1
        for weight in weights:
            
            if sum_ +weight> capacity:
                day_+=1
                sum_=0
            sum_+=weight
        return  day_<=days