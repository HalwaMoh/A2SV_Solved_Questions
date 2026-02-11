class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

     
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]

            if first != second and freq[first] == int(first) and freq[second] == int(second):
                return first + second  

        return "" 
