class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        from collections import Counter
        freq = Counter()
        left = 0
        count = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count
