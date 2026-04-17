class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        mod=10 **9 +7
        from bisect import bisect_left,bisect_right
        arr=[]
        cost=0
        for num in instructions:
            left=bisect_left(arr,num)
            right=len(arr)- bisect_right(arr,num)
            cost+= min(left,right)
            cost %=mod
            arr.insert(left,num)
            
        return cost    

                     


     
        
        