class Solution(object):
    def largestPerimeter(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        for i in range(n-2):            
            if nums[i] < nums[i+1] +nums[i+2]:

                return  nums[i]+ nums[i+1] + nums[i+2] 
            
        return 0          
           

        
        
