def maxProfit( prices: list[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:

    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

    use dynamic programming for this solution
    """


    """
    On every day, we buy the share with the price as low as we can, and sell the share with price as high as we can. 
    For the second transaction, we integrate the profit of first transaction into the cost of the second buy, 
    and then the profit of the second sell will be the total profit of two transactions.
    """
    if len(prices) < 2:
        return 0
    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0
    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        buy2 = min(buy2, price - sell1)
        sell2 = max(sell2, price - buy2)
    return sell2 



# output 6
print(maxProfit([3,3,5,0,0,3,1,4]))

# output 2
print(maxProfit([2,1,2,0,1]))