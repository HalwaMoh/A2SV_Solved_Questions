class Solution(object):
    def permute(self, nums):
        ans=[]
        def backtrack(permutation):
            if len(permutation) ==len(nums):
                ans.append(permutation[:])

                return
            for num in nums:
                if num in permutation:
                    continue
                permutation.append(num)
                backtrack(permutation)
                permutation.pop()
        backtrack([])  
        return ans


        