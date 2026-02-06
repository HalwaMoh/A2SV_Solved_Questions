class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count > n // 2:   # strictly greater
                return num
