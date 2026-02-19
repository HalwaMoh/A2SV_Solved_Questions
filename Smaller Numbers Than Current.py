class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res=[]
        n=len(nums)
        count=0
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]<nums[i]:
                    count+=1
            res.append(count)
        return res            
                    

        
        
        
