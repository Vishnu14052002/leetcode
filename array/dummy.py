class Solution:
    def dummy(self, prices):
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            tempmax = prices[i] - min_price
            if max_profit < tempmax:
                max_profit = tempmax
        print(max_profit, min_price)

            





obj = Solution()
prices = [7,6,4,3,1]
obj.dummy(prices)

