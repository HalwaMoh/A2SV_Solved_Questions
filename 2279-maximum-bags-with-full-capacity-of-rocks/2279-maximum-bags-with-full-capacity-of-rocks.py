class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        cnt=0 
        need=[] 
        for i in range(len(rocks)):
            ans=capacity[i]-rocks[i]
            need.append(ans)
        need.sort()
        for n in need:
            if n==0:     
                cnt+=1
            elif  additionalRocks >=n:
                additionalRocks-=n
                cnt+=1
            else:
                break        
        return cnt        

