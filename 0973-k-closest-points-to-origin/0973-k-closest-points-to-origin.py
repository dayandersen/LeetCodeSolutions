class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = (point[0] ** 2) + (point[1] ** 2)
            heap.append((dist, point))
        heapify(heap)
        
        k_closest = nsmallest(k, heap)
        
        return [point[1] for point in k_closest]