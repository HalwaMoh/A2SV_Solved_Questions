
from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        original = []

        for x in sorted(count):
           
            if count[x] > count[2*x]:
                return []
            
        
            for _ in range(count[x]):
                original.append(x)
                count[2*x] -= 1

        return original

         
