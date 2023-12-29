class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0

        for i in range(k+1):
            tmp_prices = prices.copy()
            for s,d,price in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + price < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + price
            prices = tmp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]