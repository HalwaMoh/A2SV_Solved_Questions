class Solution:
    def splitString(self, s: str) -> bool:
       
               
        def dfs(idx,prev):
            if idx==len(s):
                return True
            num=0
            for j in range(idx,len(s)):
                num=num*10 + int(s[j])
                if num==prev-1:
                    if dfs(j+1,num):
                        return True
                if num>=prev:
                    break
            return False
        for i in range(1,len(s)):
            first=int(s[:i])
            if dfs(i,first):
                return True
        return False            


        