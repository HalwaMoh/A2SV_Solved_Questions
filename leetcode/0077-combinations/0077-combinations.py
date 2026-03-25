class Solution(object):
    def combine(self, n, k):
        ans=[]
        def backtrack(start,comp):
            
            if len(comp)==k:
                ans.append(comp[:])
                return
            for nc in range(start,n+1):
                comp.append(nc)
                backtrack(nc+1,comp)
                comp.pop()
        backtrack(1,[])
        return ans        

        
        