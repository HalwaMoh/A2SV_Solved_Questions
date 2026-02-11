class Solution(object):
    def restoreString(self, s, indices):
        n=len(s)
        res = [''] * n
        for i in range(n):
            res[indices[i]] = s[i]
        return ''.join(res)
