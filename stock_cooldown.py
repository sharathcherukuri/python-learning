def maxProfit(prices):
    profit =0
    profit_f = 0
    i=1
    while i < len(prices):
        print(i)
        if prices[i] > prices[i-1] and profit_f < prices[i]-prices[i-1]:
            profit_f = prices[i]-prices[i-1]
            profit+= prices[i]-prices[i-1]
            i+=3
        else:
            pass

    print(profit)
    
