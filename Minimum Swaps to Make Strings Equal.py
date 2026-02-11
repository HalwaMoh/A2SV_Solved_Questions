class Solution(object):
    def minimumSwap(self, s1, s2):
       
        xy = 0
        yx = 0
        
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
       
        if (xy + yx) % 2 == 1:
            return -1
        
       
        swaps = xy // 2 + yx // 2
        swaps += xy % 2 * 2  
        return swaps

        
