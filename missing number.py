class Solution(object):
    def missingNumber(self, nums):
      
        n = len(nums)
        totalsum = n * (n + 1) // 2
        actualsum = 0

        for i in range(n):
            actualsum += nums[i]

        return totalsum - actualsum
