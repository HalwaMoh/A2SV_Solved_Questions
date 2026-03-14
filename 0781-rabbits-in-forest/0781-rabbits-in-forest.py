from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        res = 0
        
        for k, v in count.items():
            group = k + 1
            groups = (v + group - 1) // group
            res += groups * group
        
        return res

        