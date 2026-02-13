class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        count=0
       
        for row in grid:
            for num in row:
                if num < 0:
                    count+=1
        return count


        
