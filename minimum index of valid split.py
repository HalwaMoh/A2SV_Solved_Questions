class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num] > n//2:
                dominant = num
                break
        count_left = 0
        for i in range(n-1):  
            if nums[i] == dominant:
                count_left += 1
            left_len = i + 1
            right_len = n - left_len
            if count_left * 2 > left_len and (freq[dominant] - count_left) * 2 > right_len:
                return i
        return -1

        
