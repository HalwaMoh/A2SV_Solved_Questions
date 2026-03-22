class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
       
        n = len(nums)
        counts = Counter(nums)
        dom, dom_count = max(counts.items(), key=lambda item : item[1])

        left_count = 0
        for i in range(n):
            if nums[i] == dom:
                left_count += 1

            right_count = dom_count - left_count
            left_length = i + 1
            right_length = n - left_length
            
            if left_count > (left_length // 2) and right_count > (right_length // 2):
                return i

        return -1
        