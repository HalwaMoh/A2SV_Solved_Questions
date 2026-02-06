class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, val in freq.items():
            if val == 1:
                return key
