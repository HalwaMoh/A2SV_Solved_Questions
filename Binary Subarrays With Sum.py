class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

       
        prefix_sum = 0
        hashmap = {0:1}
        count = 0

        for num in nums:
            prefix_sum += num
            
            if prefix_sum - goal in hashmap:
                count += hashmap[prefix_sum - goal]

            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
