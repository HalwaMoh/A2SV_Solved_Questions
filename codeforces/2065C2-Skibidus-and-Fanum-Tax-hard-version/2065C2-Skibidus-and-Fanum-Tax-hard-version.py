import bisect
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    prev=-float('inf')
    ok=True
    for x in a:
        choice=[]
        if x >= prev:
            choice.append(x)
        target=prev+x 
        index=bisect.bisect_left(b,target)
        if index < m:
            val=b[index] -x
            if val >= prev:
                choice.append(val)
        if not choice:
            ok=False 
            break   
        prev=min(choice)
    print("YES" if ok else "NO")