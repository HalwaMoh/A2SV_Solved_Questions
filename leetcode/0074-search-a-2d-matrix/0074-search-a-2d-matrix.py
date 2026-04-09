class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        left=0
        right=(r*c)-1
        while left <= right:
            mid=(left+right)//2
            if matrix[mid//c][mid % c] == target:
                return True
            elif matrix[mid//c][mid % c] < target:
                left=mid+1
            else:
                right=mid-1    
        return False            
        