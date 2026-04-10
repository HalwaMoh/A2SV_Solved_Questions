class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.canallocatecandy(candies, k, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def canallocatecandy(self, candies, k, no_of_candy):
        count = 0
        
        for c in candies:
            count += c // no_of_candy
            if count >= k:
                return True
        
        return False