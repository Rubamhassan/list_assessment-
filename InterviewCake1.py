"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday."""

def get_max_profit(stock_prices_yesterday):
    
    max_profit = 0
    
    for outer_time in xrange(len(stock_prices_yesterday)):
        for inner_time in xrange(len(stock_prices_yesterday)):
            earlier_time = min(outer_time, inner_time)
            later_time = maz(outer_time, inner_time)
            
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price = stock_prices_yesterday[later_time]
            
            profit = later_price - earlier_price
            max_profit = max(max_profit, potential_profit)
	return max_profit







