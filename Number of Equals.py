n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
count = 0

while i < n and j < m:
    if a[i] == b[j]:
        value = a[i]

        count_a = 0
        while i < n and a[i] == value:
            count_a += 1
            i += 1

        count_b = 0
        while j < m and b[j] == value:
            count_b += 1
            j += 1

        count += count_a * count_b

    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(count)
