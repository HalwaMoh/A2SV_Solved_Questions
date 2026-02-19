class Solution:
    def largestNumber(self,nums):
        num=list(map(str,nums))
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if num[j]+num[j+1] < num[j+1]+num[j]:
                    num[j], num[j+1] = num[j+1], num[j]
        result= ''.join(num)   
        if result[0]=='0':
            return '0'
        return result    
             
