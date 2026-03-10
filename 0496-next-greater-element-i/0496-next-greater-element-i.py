class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                hashmap[prev] = num
            stack.append(num)

        for num in stack:
            hashmap[num] = -1

        result = []
        for num in nums1:
            result.append(hashmap[num])

        return result