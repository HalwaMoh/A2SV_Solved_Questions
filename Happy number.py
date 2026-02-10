class Solution(object):
    def isHappy(self, n):
        
        var = set()
        while n != 1 and n not in var:
            var.add(n)
            s = 0
            while n > 0:
                digit = n % 10
                s += (digit*digit)
                n /= 10
            n = s
        return (n == 1)
