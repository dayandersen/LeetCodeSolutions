class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid.insert(0, [10000000] * (n+1))
        for i in range(m+1):
            grid[i].insert(0, 1000000)

        q = deque()
        seen = {}
        def check(r,c):
            if r <= m and c <= n and (r,c) not in seen:
                return True
            return False
        if check(2,0):
            q.append((2,0))
        if check(0,2):
            q.append((0,2))
        
        while(q):
            row,col = q.popleft()
            if not check(row, col):
                continue
            seen[(row, col)] = True
            up = grid[row-1][col]
            left = grid[row][col-1]
            curr = grid[row][col]

            grid[row][col] = min(up + curr, left + curr)
            q.append((row+1,col))
            q.append((row,col+1))
        return grid[m][n]
