import sys
def sellStock(prices):
    minprice = sys.maxsize
    #print(minprice)
    max_profit = 0
    t_profit = 0

    for i in range(0,len(prices)):
        if minprice > prices[i]:
            minprice = prices[i]
        elif max_profit < prices[i] - minprice :
            max_profit = prices[i] - minprice
            t_profit += max_profit
    print( max_profit)
            
