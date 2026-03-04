n,k,q=map(int,input().split())
max_=200000
freq=[0]*(max_ +2)
for _ in range(n):
    l,r=map(int,input().split())
    freq[l]+=1
    freq[r+1]-=1
coverage=[0]*(max_+2)
for i in range(max_+1):
    coverage[i]=coverage[i-1] + freq[i]
admissible=[0]*(max_+2)
for i in range(max_+1):
    if coverage[i]>=k:
        admissible[i]=1
prefix=[0]*(max_+2) 
for i in range(max_+1):
    prefix[i]=prefix[i-1] + admissible[i]    

for _ in range(q):
    a,b=map(int,input().split())
    print(prefix[b] -prefix[a-1])
    

