

t = int(input())
for _ in range(t):
    n = int(input())
    str = input()

    ans = -1

    for i in range(n):
        for length in range(2,8):   
            if i + length > n:
                break

            substr = str[i:i+length]

            if substr.count('a') > substr.count('b') and substr.count('a') > substr.count('c'):
                ans = length
                break

        if ans != -1:
            break

    print(ans)
