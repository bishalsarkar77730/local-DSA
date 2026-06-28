# given [
#     array prices
#     prices[i] is the stock price on day 1
# ]

# conditions [
#     Not allow to sell at day 1
# ]

prices = [7,6,4,3,1]


def brute_Best_time_to_buy_and_sell_stock():
    n = len(prices)
    if n < 2:
        return 0
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    print(max_profit)


brute_Best_time_to_buy_and_sell_stock()
