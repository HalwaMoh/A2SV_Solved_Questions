class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3 != 0:
            return []
        middle=num//3
        return [middle -1 ,middle, middle +1]    

