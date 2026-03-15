t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max_=a[-1]
    ans=0
    for k in range(2,n):
        i=0
        j=k-1
        while i<j:
            if a[i]+a[j]>a[k] and a[i]+a[j]+a[k] >max_:
                ans+=(j-i)
                j-=1
            else:
                i+=1
    print(ans)