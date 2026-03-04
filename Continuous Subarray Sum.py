class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}  
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in remainder_map:
                if i - remainder_map[prefix_sum] >= 2:
                    return True
            else:
                remainder_map[prefix_sum] = i
        
        return False
