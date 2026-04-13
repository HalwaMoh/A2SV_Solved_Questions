n = int(input())
children = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    p = int(input())
    children[p].append(i)


for node in range(1, n + 1):
    if children[node] == []:
        continue 
    
    leaf_count = 0
    
    for child in children[node]:
        if children[child] == []:
            leaf_count += 1
    
    if leaf_count < 3:
        print("No")
        exit()

print("Yes")