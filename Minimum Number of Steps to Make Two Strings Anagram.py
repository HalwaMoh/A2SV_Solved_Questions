class Solution(object):
    def minSteps(self, s, t):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        ans = 0
        for x in freq:
            if x > 0:
                ans += x

        return ans



        
        
