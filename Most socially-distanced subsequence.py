t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    result = [p[0]]
    
    for i in range(1, n-1):
        if (p[i] - p[i-1]) * (p[i+1] - p[i]) < 0:
            result.append(p[i])
    
    result.append(p[-1])
    
    print(len(result))
    print(*result)
