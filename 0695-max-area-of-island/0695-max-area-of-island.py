class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxx = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1],]
        n, m = len(grid), len(grid[0])
        def explore(row,col):
            if row >= 0 and row < n and col >= 0 and col < m and grid[row][col] == 1:
                grid[row][col] = -1
                return 1 + sum(explore(row+d[0], col+d[1]) for d in directions)
            else:
                return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.maxx = max(explore(i,j), self.maxx)
        return self.maxx