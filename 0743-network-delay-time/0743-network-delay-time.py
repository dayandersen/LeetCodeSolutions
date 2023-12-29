class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = [[] for _ in range(n+1)]

        for src,dest,cost in times:
            adjList[src].append([dest,cost])

        min_heap = [(0,k)]
        visited = {}
        cost = 0
        while min_heap:
            path_cost, node_n = heappop(min_heap)
            if node_n in visited:
                continue
            visited[node_n] = True
            cost = max(cost, path_cost)
            for neighbor_n, neighbor_p in adjList[node_n]:
                heappush(min_heap, (path_cost+neighbor_p, neighbor_n))

        if len(visited) != n:
            return -1
        else:
             return cost