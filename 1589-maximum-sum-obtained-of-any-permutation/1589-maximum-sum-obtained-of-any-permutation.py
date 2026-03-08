class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        count = [0]*(n+1)

        for l,r in requests:
            count[l] += 1
            count[r+1] -= 1

        for i in range(1,n):
            count[i] += count[i-1]

        count = count[:-1]

        nums.sort()
        count.sort()

        ans = 0
        mod = 10**9+7

        for i in range(n):
            ans += nums[i]*count[i]

        return ans % mod