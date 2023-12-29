class MedianFinder:

    def __init__(self):
        #big min heap
        self.min_heap = []
        #smol max heap
        self.max_heap = []
        heapify(self.min_heap)
        heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heappush(self.min_heap, num)
        elif not self.min_heap:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -1 * num)

        if len(self.max_heap) - len(self.min_heap) >= 2:
            #rebalance
            c = heappop(self.max_heap)
            heappush(self.min_heap, -1 * c)
        elif len(self.min_heap) - len(self.max_heap) >= 2:
            c = heappop(self.min_heap)
            heappush(self.max_heap, -1 * c)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -1 * self.max_heap[0]
            else:
                return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()