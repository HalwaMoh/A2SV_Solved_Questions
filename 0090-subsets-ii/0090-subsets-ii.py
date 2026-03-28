class Solution(object):
    def subsetsWithDup(self, nums):
        ans=[]
        nums.sort()
        def backtrack(start,subset):
            ans.append(subset[:])
            
            for i in range(start,len(nums)):
                if i >start and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans    

        
        

        