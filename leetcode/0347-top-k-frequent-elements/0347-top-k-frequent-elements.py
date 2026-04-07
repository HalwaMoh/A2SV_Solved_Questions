class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
