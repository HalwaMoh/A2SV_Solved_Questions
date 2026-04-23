class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        perimeter=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    for dr, dc in direction:
                        nr, nc=r + dr , c+ dc
                        if nr <0 or nr >= row or nc <0 or nc>= col or grid [nr][nc]==0:
                            perimeter +=1
        return perimeter                    
