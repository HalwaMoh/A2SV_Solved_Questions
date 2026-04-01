class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
       
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()
        
        stack = [] 
        healths = [h for _, h, _, _ in robots]
        
        for i, (_, _, d, _) in enumerate(robots):
            if d == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]
                    
                    if healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    elif healths[j] < healths[i]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()
                    else:
                        healths[i] = 0
                        healths[j] = 0
                        stack.pop()
                        break
                
        result = []
        for i, (_, _, _, original_idx) in enumerate(robots):
            if healths[i] > 0:
                result.append((original_idx, healths[i]))
        
        result.sort()
        return [h for _, h in result]
            