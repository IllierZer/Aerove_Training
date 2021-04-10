import numpy as np
d=int(input())
prices=np.zeros([d])
for i in range(d):
    prices[i]=int(input())
buy_price=np.amin(prices)
sell_price=np.amax(prices)
buy_date=np.where(prices==buy_price)
print(sell_price-buy_price)
print(buy_date[0][0]+1)

