import matplotlib.pyplot as plt
import numpy as np

symbol = 'DMC'

file = open('stock_data/'+symbol+'.csv', 'r')
linelist = file.readlines()

z = np.zeros(len(linelist), dtype=np.uint64)
p = np.zeros(len(linelist), dtype=float)
i = 0

for x in linelist:
    y = x.split(',')
    z[i] = y[1]
    p[i] = y[2]
    i = i+1

print max(p)

plt.plot(p)
plt.title('Stock Price of PSE:'+symbol+' per minute')
plt.xlim([0, len(p)])
plt.ylim([min(p), max(p)])
plt.ylabel('Price(PHP)')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
plt.show()