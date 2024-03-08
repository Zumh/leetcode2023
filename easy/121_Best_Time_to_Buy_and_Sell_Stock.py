 
def maxProfit( prices: list[int]) -> int:
    """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    max_profit = 0
    min_price = float('inf')

    """
    It iterates through the prices, keeps track of the minimum price seen so far,
    and updates the maximum profit if the current price minus the minimum price
    is greater than the maximum profit seen so far.
    """

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
print(maxProfit([7,1,5,3,6,4]))