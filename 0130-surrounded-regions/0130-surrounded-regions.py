class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        DIRS = [[0,1],[0,-1],[-1,0],[1,0],]

        def in_bounds(pot_row,pot_col):
            return pot_row >= 0 and pot_row < rows and pot_col >= 0 and pot_col < cols

        def dfs(row, col):
            board[row][col] = "o"
            for direction in DIRS:
                pot_row = row + direction[0]
                pot_col = col + direction[1]
                if in_bounds(pot_row, pot_col) and board[pot_row][pot_col] == "O":
                    dfs(pot_row, pot_col)
                        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0, rows-1] or col in [0, cols-1]):
                    dfs(row, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "o":
                    board[row][col] = "O"
        return board