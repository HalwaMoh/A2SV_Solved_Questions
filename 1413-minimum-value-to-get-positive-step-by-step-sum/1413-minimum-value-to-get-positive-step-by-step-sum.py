class Solution(object):
    def minStartValue(self, nums):
        prefix_sum=0
        min_=0
        for i in range(len(nums)):
            prefix_sum +=nums[i]
            min_=min(min_,prefix_sum)
        return 1- min_      




        
        