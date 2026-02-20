n=int(input())
x=list(map(int,input().split()))
x.sort()
if n %2 !=0:
    res=x[n//2] 
   
else:
    res=x[n//2 -1]
print(res)       


