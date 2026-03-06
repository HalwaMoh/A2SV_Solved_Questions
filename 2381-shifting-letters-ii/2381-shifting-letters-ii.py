class Solution(object):
    def shiftingLetters(self, s, shifts):
        
        n = len(s)
        diff = [0]*(n+1)

        for start, end, d in shifts:
            val = 1 if d == 1 else -1
            diff[start] += val
            diff[end+1] -= val

        cur = 0
        res = []

        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(new_char + ord('a')))

        return "".join(res)
        