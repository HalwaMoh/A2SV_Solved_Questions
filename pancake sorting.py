class Solution(object):
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    arr[:max_index+1] = arr[:max_index+1][::-1]
                    res.append(max_index + 1)
                arr[:size] = arr[:size][::-1]
                res.append(size)
        return res
