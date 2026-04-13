class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i=0
        upto=0
        ans=0
      
        while upto <n:
            if i< len(nums) and nums[i] <= upto +1:
                upto +=nums[i]
                i+=1
            else:
                ans+=1
                upto += (upto +1)
        return ans            
        