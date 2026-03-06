class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        hashmap = {0:1}
        count = 0

        for num in nums:
            prefix_sum += num
            reminder=prefix_sum %k
            if reminder in hashmap:
                count += hashmap[reminder]

            hashmap[reminder] = hashmap.get(reminder, 0) + 1

        return count
        
