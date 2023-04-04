# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example: prices = [7,1,5,3,6,4] Return: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


# code here
# O(n)
def buy_and_sell_stock(prices: list):
    max_sum = 0
    curr_sum = 0

    for i in range(len(prices) - 1):
        curr_sum = curr_sum + prices[i + 1] - prices[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

test_prices = [7, 1, 5, 3, 6, 4]  # 5
test_result = buy_and_sell_stock(test_prices)
print(test_result)
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).
# Example: prices = [7,1,5,3,6,4] Return: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


# code here
# O(n)
def buy_and_sell_stock(prices):
    maximum = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            maximum = maximum + prices[i + 1] - prices[i]

    return maximum

test_prices = [7, 1, 5, 3, 6, 4]  # Return: 7
test_result = buy_and_sell_stock(test_prices)
print(test_result)