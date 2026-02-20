class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n=len(citations)
        if n % 2 ==1:
             res=citations[n//2]
        else:
            res=citations[n//2-1]
        return res    


           
       


       
        
