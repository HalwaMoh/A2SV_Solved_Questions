class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        left=0
        right=n-1
        while left <= right:
            mid=(left+right)//2
            paper_remaining=n-mid
            if citations[mid] >= paper_remaining:
                right=mid-1
            else:
                left=mid+1
        return n- left            
      