class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        q = deque()
        # m = row
        # n = col
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid.insert(0,([0] * n))
        for i in range(m+1):
            obstacleGrid[i].insert(0,0)

        seen = {}
        grid = []
        for i in range(m+1):
            grid.append([0] * (n+1))
            
        def check(pot_row, pot_col):
            if pot_row <= m and pot_col <= n and (pot_row, pot_col) not in seen and obstacleGrid[pot_row][pot_col] != 1:
                return True
            return False
        
        if check(1,1):
            grid[1][1] = 1
        if check(2,0):
            q.append((2,0))
        if check(0,2):
            q.append((0,2))
        
        while q:
            row,col = q.popleft()
            if not check(row, col):
                continue
            seen[(row,col)] = True
            grid[row][col] = grid[row-1][col] + grid[row][col-1]
            q.append((row+1, col))
            q.append((row, col+1))
        return grid[m][n]