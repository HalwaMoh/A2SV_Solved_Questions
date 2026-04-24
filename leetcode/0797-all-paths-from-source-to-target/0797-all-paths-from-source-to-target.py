class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res=[]
        path=[0]
        def dfs(node):
            if node==len(graph)-1:
                res.append(path.copy())
                return
            for neghibor in graph[node]:
                path.append(neghibor)
                dfs(neghibor)
                path.pop()
        dfs(0)
        return res           