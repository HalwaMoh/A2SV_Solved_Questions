class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        seen=[False]* (n+1)
        for num in nums:
            if num <= n and num>0:
                seen[num]=True
        for i in range(1,n+1):
            if not seen[i]:
                return i
        return n+1                
            
                
            



        