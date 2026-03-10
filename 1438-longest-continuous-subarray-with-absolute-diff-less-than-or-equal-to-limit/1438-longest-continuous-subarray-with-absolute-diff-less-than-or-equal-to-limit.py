from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        max_q = deque()  
        min_q = deque()  
        left = 0
        ans = 0

        for right in range(len(nums)):
            curr = nums[right]

           
            while max_q and max_q[-1] < curr:
                max_q.pop()
            max_q.append(curr)

           
            while min_q and min_q[-1] > curr:
                min_q.pop()
            min_q.append(curr)

            
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans