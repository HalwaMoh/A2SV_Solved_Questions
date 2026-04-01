class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        
        def helper(num1, num2, remaining):
            while remaining:
                sum_ = str(num1 + num2)
                if not remaining.startswith(sum_):
                    return False
                remaining = remaining[len(sum_):]
                num1, num2 = num2, int(sum_)
            return True

     
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]

                
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue

                if helper(int(num1), int(num2), num[j:]):
                    return True
        return False