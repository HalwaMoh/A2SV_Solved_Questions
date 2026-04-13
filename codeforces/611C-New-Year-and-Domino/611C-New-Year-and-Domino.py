import sys
input = sys.stdin.readline

h, w = map(int, input().split())
g = [input().strip() for _ in range(h)]

hor = [[0]*w for _ in range(h)]
ver = [[0]*w for _ in range(h)]

# build
for i in range(h):
    for j in range(w):
        if j+1 < w and g[i][j] == '.' and g[i][j+1] == '.':
            hor[i][j] = 1
        if i+1 < h and g[i][j] == '.' and g[i+1][j] == '.':
            ver[i][j] = 1


ph = [[0]*(w+1) for _ in range(h+1)]
pv = [[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        ph[i+1][j+1] = hor[i][j] + ph[i][j+1] + ph[i+1][j] - ph[i][j]
        pv[i+1][j+1] = ver[i][j] + pv[i][j+1] + pv[i+1][j] - pv[i][j]

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

  
    h_ans = ph[r2][c2-1] - ph[r1-1][c2-1] - ph[r2][c1-1] + ph[r1-1][c1-1]


    v_ans = pv[r2-1][c2] - pv[r1-1][c2] - pv[r2-1][c1-1] + pv[r1-1][c1-1]

    print(h_ans + v_ans)