

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for _ in range(n)]
    

    casinos.sort()
    
    current = k
    i = 0
    
    while True:
        best = current

        while i < n and casinos[i][0] <= current:
            l, r, real = casinos[i]
            if current <= r:
                best = max(best, real)
            i += 1
        
        if best == current:
            break 
        current = best
    
    print(current)
        
