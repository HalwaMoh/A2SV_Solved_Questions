def dfs(i, cur):
    global good
    if i == q:
        if cur == target:
            good += 1
        return
    
    dfs(i + 1, cur + 1)
    dfs(i + 1, cur - 1)

dfs(0, pos)

print(good / float(total))