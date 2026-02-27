n, s = map(int, input().split())
a = list(map(int, input().split()))

left = 0
curr_sum = 0
min_len = float('inf')

for right in range(n):
    curr_sum += a[right]

   
    while curr_sum >= s:
        min_len = min(min_len, right - left + 1)
        curr_sum -= a[left]
        left += 1

if min_len == float('inf'):
    print(-1)
else:
    print(min_len)
