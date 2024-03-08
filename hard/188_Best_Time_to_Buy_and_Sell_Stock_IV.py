def maxProfit( k: int, prices: list[int]) -> int:
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


    Example 1:

    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    Example 2:

    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

    use dynamic programming for this solution
    """

    """
    Dynamic programming 
    It initialize a 3D array to store the maximum profit at each day,
    with different states for holding or not holding a stock.
    and for different numbers of transactions.
    Then, it iterates through the prices and updates the profit at each day.
    Finally, it returns the maximum profit for making at most k transactions.
    """

    n = len(prices)
    if n < 2:
        return 0
    dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        for j in range(1, k+1):
            if i == 0:
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i]
                continue
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
    return dp[n-1][k][0]

    
# output 2
print(maxProfit(2, [2, 4, 1]))

# output 7
print(maxProfit(2, [3,2,6,5,0,3]))