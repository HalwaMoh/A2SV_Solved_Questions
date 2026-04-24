from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph=defaultdict(list)
        for i in range(n):
            x1 ,y1,r1 =bombs[i]
            for j in range(n):
                if i ==j :
                    continue
                x2 ,y2, _ =bombs[j]
                dx = x1 - x2 
                dy = y1- y2
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)
        def dfs(node,visited):
            visited.add(node)
            cnt =1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    cnt += dfs(neighbor,visited)
            return cnt
        res=0
        for i in range(n):
            visited=set()
            res=max(res,dfs(i,visited))    
        return res                        
