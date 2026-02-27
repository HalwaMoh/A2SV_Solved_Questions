from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
count = 0
freq = Counter()

for right in range(n):
    freq[a[right]] += 1

    
    while len(freq) > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        left += 1

   
    count += (right - left + 1)

print(count)
