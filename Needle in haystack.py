from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    t = input().strip()

    cs = Counter(s)
    ct = Counter(t)

 
    if any(cs[c] > ct[c] for c in cs):
        print("Impossible")
        continue

    for c in s:
        ct[c] -= 1


    remaining = []
    for c in sorted(ct.keys()):
        if ct[c] > 0:
            remaining.append(c * ct[c])
    remaining = "".join(remaining)


    res = []
    inserted = False
    for c in remaining:
        if not inserted and c >= s[0]:
            res.append(s)
            inserted = True
        res.append(c)
    if not inserted:
        res.append(s)

    print("".join(res))
