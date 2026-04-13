class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        mx = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= mx:
                mx = nums[i]
            else:
                k = ceil(nums[i] /mx)  
                ans += (k - 1)
                mx = nums[i] // k
        
        return ans