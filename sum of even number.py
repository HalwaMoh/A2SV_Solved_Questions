class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        res = []

        for i in range(len(queries)):
            val = queries[i][0]
            index = queries[i][1]
            nums[index] += val
            s = 0
            for n in nums:
                if n % 2 == 0:
                    s += n

            res.append(s)

        return res
