class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        val = 0
        out = []
        self.dfs(val, out, n)
        return out
    
    def dfs(self, curr, out, n):
        start_range = 1
        if (curr != 0):
            out += [curr]
            start_range = 0
        
        for i in range(start_range,10):
            if (curr * 10) + i <= n:
                self.dfs((curr*10) + i, out, n)
            else:
                return