from collections import defaultdict
class Solution(object):

    def validPath(self, n, edges, source, destination):
        graph=defaultdict(list)
        for node1 , node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited=set()
        return self.dfs(source,destination,graph,visited)
    def dfs(self,node,destination,graph,visited):
        if node==destination:
            return True
        visited.add(node)    
        for neghibor in graph[node]:
            if neghibor not in visited:
                found=self.dfs(neghibor,destination,graph,visited)
                if found:
                    return True
        return False            
