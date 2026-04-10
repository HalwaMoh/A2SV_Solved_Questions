class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(start, sub):
            if len(sub) >= 2:
                ans.append(sub[:])
            used = set() 
            for i in range(start, len(nums)):
                if sub and nums[i] < sub[-1]:
                    continue
                if nums[i] in used:
                    continue
                used.add(nums[i])
                
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()
        
        backtrack(0, [])
        return ans