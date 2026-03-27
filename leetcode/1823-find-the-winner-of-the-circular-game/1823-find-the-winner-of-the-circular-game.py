class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums=[i for i in range(1,n+1)]
        curr=0

        while len(nums)>1:
            curr=(curr + k-1) % len(nums)
            nums.pop(curr)
        return nums[0]    

       