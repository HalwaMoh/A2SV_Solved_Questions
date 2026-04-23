class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        expectedsum= n*(n + 1) // 2
        sum1=sum(nums)
       
        
        dict_={}
        duplicate=0
        for num in nums:
            dict_[num]=dict_.get(num,0) +1
            if dict_[num] >1:
                duplicate=num
        missing=expectedsum - sum1 + duplicate        

        return [duplicate,missing ]       



        