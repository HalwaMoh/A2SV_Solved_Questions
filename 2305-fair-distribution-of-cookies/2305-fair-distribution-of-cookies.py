class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribute=[0]*k
        n=len(cookies)
        def dfs(i,cnt):
            if n-i < cnt:
                return float('inf')
            if i==n:
                return max(distribute)
            ans=float('inf')

            for j in range(k):
                cnt -= int(distribute[j]==0)
                distribute[j] += cookies[i]

                ans=min(ans,dfs(i+1 ,cnt)) 

                distribute[j] -= cookies[i]
                cnt += int(distribute[j]==0)  
            return ans
        return dfs(0,k)

        