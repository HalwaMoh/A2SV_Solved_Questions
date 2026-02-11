class Solution(object):
    def findCommonResponse(self, responses):
        
        freq = {} 

        for response in responses:
            
            unique = set(response)

            for r in unique:
                freq[r] = freq.get(r, 0) + 1

        max_ = max(freq.values())

        answer = [r for r, count in freq.items() if count == max_]
        return min(answer)


             


        
