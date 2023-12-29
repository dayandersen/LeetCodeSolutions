class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row_count,col_count = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1],]
        def destructive_exploration(row_index, col_index):
            if (row_index >= 0 
            and row_index < row_count 
            and col_index >= 0 
            and col_index < col_count 
            and grid[row_index][col_index] == '1'):
                grid[row_index][col_index] = '0'
                for direction in directions:
                    destructive_exploration(row_index + direction[0], col_index + direction[1])

        for row_index in range(row_count):
            for col_index in range(col_count):
                if grid[row_index][col_index] == '1':
                    count += 1
                    destructive_exploration(row_index, col_index)
        return count