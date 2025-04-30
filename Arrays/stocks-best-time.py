"""
You are given an array prices where prices[i] is the price of a given 
stock on the ith day.
You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

# brute-force resenje, treba da uradim sa O(n) time complexity

def bestTimeStocks(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

prices = [7,1,5,3,6,4]
print(bestTimeStocks(prices))