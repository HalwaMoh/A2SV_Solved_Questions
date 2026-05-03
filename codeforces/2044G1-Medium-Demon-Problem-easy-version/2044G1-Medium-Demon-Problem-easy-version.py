from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    r = [x-1 for x in map(int, input().split())]

    indeg = [0]*n
    for i in range(n):
        indeg[r[i]] += 1

    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    depth = [0]*n
    ans = 0

    while q:
        u = q.popleft()
        v = r[u]

        indeg[v] -= 1
        depth[v] = max(depth[v], depth[u] + 1)
        ans = max(ans, depth[v])

        if indeg[v] == 0:
            q.append(v)

    print(ans + 2)