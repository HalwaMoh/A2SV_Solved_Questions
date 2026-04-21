class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        row=len(grid)
        col=len(grid[0])
        cnt=0
        def dfs(r,c):
            if r<0 or r >= row or c<0 or c>= col or grid[r][c]=='0':
                return
            grid[r][c]='0'    
            for dr,dc in direction:
                new_row,new_col=r+dr, c+dc
                dfs(new_row, new_col)    
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    cnt +=1
                    dfs(i,j)
        return cnt             