import numpy as np
import matplotlib.pyplot as plt


file = open('hist_stock_data/AC_hist.csv')
linelist = file.readlines()

p_open = np.zeros(len(linelist)-2, dtype=float)
p_close = np.zeros(len(linelist)-2, dtype=float)
p_high = np.zeros(len(linelist)-2, dtype=float)
p_low = np.zeros(len(linelist)-2, dtype=float)
i = 0
k = 0

for x in linelist:
    y = x.split(',')
    try:
        p_close[i] = float(y[1])
        p_open[i] = float(y[2])
        p_high[i] = float(y[3])
        p_low[i] = float(y[4])
    except ValueError:
        continue
    i = i+1

p_close = p_close[::-1]
p_open = p_open[::-1]
p_high = p_high[::-1]
p_low = p_low[::-1]

plt.plot(p_high, '-')
plt.plot(p_low, '--')
plt.ylim([min(p_low)-10, max(p_high)+10])
plt.xlim([0, len(p_close)])
plt.title('Historical Stock Prices for Ayala Corporation')
plt.ylabel('Price (Php)')
plt.show()