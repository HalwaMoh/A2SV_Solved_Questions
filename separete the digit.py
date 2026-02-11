class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for num in nums:
            for digit in str(num):
                res.append(int(digit))
        return res
