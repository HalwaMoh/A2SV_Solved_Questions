class Solution:

    def majorityElement(self,nums):
        from collections import defaultdict

    
        n = len(nums)
        count = defaultdict(int)
        
    
        for num in nums:
            count[num] += 1
        
       
        result = [num for num, c in count.items() if c > n // 3]
        
        return result
