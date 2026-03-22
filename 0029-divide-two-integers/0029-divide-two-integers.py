class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        
        negative = (dividend < 0) ^ (divisor < 0)

        dvd = abs(dividend)
        dvs = abs(divisor)

        result = 0

        while dvd >= dvs:
            temp = dvs
            count = 1

            
            while dvd >= temp + temp:
                temp += temp
                count += count

            dvd -= temp
            result += count

        return -result if negative else result
        