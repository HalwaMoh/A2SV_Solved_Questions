class Solution(object):
    def dividePlayers(self, skill):
        n = len(skill)
        if n % 2 != 0:
            return -1  

        skill.sort()
        total = skill[0] + skill[-1]  
        result = 0

        for i in range(n // 2):
            if skill[i] + skill[n-1-i] != total:
                return -1  
            result += skill[i] * skill[n-1-i] 

        return result
