class Solution(object):
    def customSortString(self, order, s):
        freq = {}
       
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        res = []

        for ch in order:
            if ch in freq:
                res.append(ch * freq[ch])
                del freq[ch]  

    
        for ch, count in freq.items():
            res.append(ch * count)

        return "".join(res)
