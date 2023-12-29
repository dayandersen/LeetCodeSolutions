class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [height[0]]
        max_right = [height[n-1]]
        for i in range(1, n):
            max_right.append(max(max_right[-1], height[n-1-i]))
            max_left.append(max(max_left[-1], height[i]))
        
        max_right.reverse()
        water = 0
        for i in range(1,n-1):
            water += max(min(max_left[i-1], max_right[i+1]) - height[i], 0)
        return water