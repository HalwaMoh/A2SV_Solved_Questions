from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)

    def merge(self, left_half, right_half) -> List[int]:
        i, j = 0, 0
        result = []

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1

        result.extend(left_half[i:])
        result.extend(right_half[j:])

        return result

    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2

        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return self.merge(left_half, right_half)