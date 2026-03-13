class Solution(object):
    def find132pattern(self, nums):
        stack=[]
        sec_=float('-inf')
        for num in reversed(nums):
            if num<sec_:
                return True
            while stack and stack[-1]<num :
                sec_=stack.pop()
            stack.append(num)
        return False               

        