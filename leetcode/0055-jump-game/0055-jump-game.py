class Solution(object):
    def canJump(self, nums):
        jump=0
        for i in range(len(nums)):
            if i>jump:
                
                return False 
            jump=max(jump,i+nums[i])
        
        else:  
            return True    
        
        