class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heappush(h, i)
        
        for i in range(len(nums)-k):
            heappop(h)
        return h[0]