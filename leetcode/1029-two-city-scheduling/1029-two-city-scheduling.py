class Solution(object):
    def twoCitySchedCost(self, costs):
        
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)// 2
        tot = 0
        for i in range(len(costs)):
            if i < n:
                tot+=costs[i][0]   
            else:
                tot+=costs[i][1]   
        return tot