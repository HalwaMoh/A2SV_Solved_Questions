class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        duplicate=0
        for num in nums:
            if num in seen:
                duplicate=num
            seen.add(num)
        return duplicate        

        