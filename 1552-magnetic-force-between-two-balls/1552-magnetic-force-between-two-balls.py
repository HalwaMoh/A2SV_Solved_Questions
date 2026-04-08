import math
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans=0
        n=len(position)
        position.sort()
        low=1
        high=ceil(position[n - 1] / (m - 1)) 
        while low <=high:
            mid=(low+high)//2
            
            if self.canplaceballs(mid,position,m):
                ans=mid
                low=mid+1
            else:
                high=mid-1  
        return ans

    def canplaceballs(self,x,pos,m):
        prev=pos[0]
        count=1
        for i in range(len(pos)):
            if pos[i]-prev>=x:
                count+=1
                prev=pos[i]
                
            if count==m:
                return True
        return False            

                  



        