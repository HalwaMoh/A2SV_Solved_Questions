t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pref = 0
    first_hit = -1
    cycle = -1

   
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1

        if pref == -x and first_hit == -1:
            first_hit = i + 1

        if pref == 0 and cycle == -1:
            cycle = i + 1

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    if cycle == -1:
        print(1)
        continue

    ans = 1 + (k - first_hit) // cycle
    print(ans)
