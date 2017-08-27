file = open('hist_stock_data/AC_hist.csv')
linelist = file.readlines()
file.close()

for x in linelist:
    y = x.split(',')


