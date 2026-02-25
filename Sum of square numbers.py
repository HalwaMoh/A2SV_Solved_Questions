class Solution(object):
    def judgeSquareSum(self, c):
        a=0
        b=int(sqrt(a))
        while a<=b:
            total=a**2 +b**2
            if total ==c:
                return True
            elif total < c:
                a+=1
            else:
                b-=1
        return False            

        


    
        
