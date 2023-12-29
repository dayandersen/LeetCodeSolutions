class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # Prim's approach
        # You have a node pool, need to find the minimum edge to a node not currently in the node pool
        # To do this we could have a heap of all edges, and eliminate those edges that have dst in the node pool

        manhattan = lambda x1, x2: abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

        # This will end up being a map, of src -> dst -> cost {0: {1: 2, 2: 4}}
        adj_list = {}
        visit = {}
        for i in range(n):
            temp = {}
            for j in range(n):
                temp[j] = manhattan(points[i],points[j])
            adj_list[i] = temp
        
        # Composed of (cost, dest) tuples
        heap = []
        for dest, cost in adj_list[0].items():
            heap.append((cost, dest))
        heapify(heap)
        visit[0] = True
        total_cost = 0
        while(heap):
            cost, dest = heappop(heap)

            if dest in visit:
                continue
                
            visit[dest] = True
            for d, c in adj_list[dest].items():
                if d not in visit:
                    heappush(heap, (c, d))
            total_cost += cost

        return total_cost