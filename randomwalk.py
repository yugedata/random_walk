import matplotlib.pyplot as plt
import random

start = 115.50
price = start

minutes_per_day = 390
total_ticks = minutes_per_day*2

ticks = []
prices = []

for i in range(total_ticks):
    ticks.append(i)

for i in range(total_ticks):
    change = random.uniform(-.009, .009)
    price = price + change
    prices.append(price)


plt.plot(ticks, prices, label='AAPL')


plt.title('a random walk')

plt.legend()
plt.show()
