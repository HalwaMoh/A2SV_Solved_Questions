class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def mergesort(arr):
            if len(arr) <=1:
                return arr
            mid=len(arr)//2
            left=mergesort(arr[ : mid])
            right= mergesort( arr[mid: ])
            
            l,r=0,0
            merged=[]
            while l<=len(left) and r <= len(right):
                if left[l] < right[r]:
                    merged.append(left[l])
                    l +=1
                else:
                    merged.append(right[r])
                    r +=1  
            merged.extend(left[l:])
            merged.extend(right[r:] )

            return merged
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

                     


     
        
        