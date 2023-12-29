class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        out = [0] * n
        for i in range(n):
            while len(stack) != 0 and temperatures[i] > stack[-1][1]:
                index, temperature = stack.pop()
                out[index] = i - index
            stack.append([i, temperatures[i]])
        return out
