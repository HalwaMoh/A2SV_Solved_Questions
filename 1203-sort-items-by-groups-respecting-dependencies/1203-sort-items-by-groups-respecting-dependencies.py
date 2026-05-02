from collections import defaultdict, deque
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
       
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        
        item_graph = defaultdict(list)
        item_indegree = [0]*n
        
        group_graph = defaultdict(list)
        group_indegree = [0]*m
        
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    item_graph[j].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[group[j]].append(group[i])
                    group_indegree[group[i]] += 1
        
        def topo(nodes, graph, indegree):
            q = deque([x for x in nodes if indegree[x] == 0])
            res = []
            while q:
                u = q.popleft()
                res.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return res if len(res) == len(nodes) else []
        
        group_order = topo(list(range(m)), group_graph, group_indegree)
        if not group_order:
            return []
        
        group_items = defaultdict(list)
        for i in range(n):
            group_items[group[i]].append(i)
        
        res = []
        for g in group_order:
            items = group_items[g]
            order = topo(items, item_graph, item_indegree)
            if len(order) != len(items):
                return []
            res.extend(order)
        
        return res