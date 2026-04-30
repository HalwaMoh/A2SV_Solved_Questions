from collections import deque
class Solution(object):
    def getAncestors(self, n, edges):
        incoming=[0 for _ in range(n)]
        graph=[[] for _ in range(n)]
        queue=deque()
        ans=[set() for _ in range(n)]
        for i,j in edges:
            graph[i].append(j)
            incoming[j] +=1
        for i in range(n):
            if incoming[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
        
            for child in graph[node]:
                
                ans[child] |= ans[node]
                ans[child].add(node)
                incoming[child] -=1
                if incoming[child] ==0:
                    queue.append(child)
        return [sorted(list(s)) for s in ans]