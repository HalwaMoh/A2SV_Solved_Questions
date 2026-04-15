class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen={}
        res=[]
        for num in nums:
            seen[num]=seen.get(num,0) +1
            if seen[num] >1:
                res.append(num)
        return res    


        