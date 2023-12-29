class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp_prices = prices.copy()
            for s, d, price in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + price < temp_prices[d]:
                    temp_prices[d] = prices[s] + price
            prices = temp_prices

        if prices[dst] != float("inf"):
            return prices[dst]
        return -1