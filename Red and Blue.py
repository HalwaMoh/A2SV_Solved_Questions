t=int(input())

for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    prefix_sum=0
    max1=0
    max2=0

    for i in r:
        prefix_sum+=i
        max1=max(max1,prefix_sum)  
    pre_sum=0
    for i in b:
        pre_sum+=i
        max2=max(max2,pre_sum)  
    print(max1+max2)  


