class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        res = ""

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sort_ = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for ch, count in sort_:
            res += ch * count  

        return res
