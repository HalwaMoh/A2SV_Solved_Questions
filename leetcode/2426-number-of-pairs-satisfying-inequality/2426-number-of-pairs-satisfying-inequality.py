class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]

        def mergesort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, cnt_left = mergesort(arr[:mid])
            right, cnt_right = mergesort(arr[mid:])
           
            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j] < left[i] - diff:
                    j += 1
                count += len(right) - j
           
            merged = []
            l = r = 0
            
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            merged.extend(left[l:])
            merged.extend(right[r:])
            
            return merged, cnt_left + cnt_right + count

        _, res = mergesort(arr)
        return res