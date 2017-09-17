import urllib
import json

symbols = open("stocks.txt").read()
symbols = symbols.split("\n")

for symbol in symbols:
    try:
        file = open("stock_data/" + symbol + ".csv", "r")
        linelist = file.readlines()
        file.close()
        last_line = linelist[-1]
        last_line_array = last_line.split(',')
        last_line_data = last_line_array[1]

    except IOError:
        file = open("stock_data/" + symbol + ".csv", "w")

    htmltext = urllib.urlopen("https://www.bloomberg.com/markets/chart/data/1D/"+symbol+":PM")
                    # https://www.bloomberg.com/markets/watchlist/recent-ticker/DD:PM
    data = json.load(htmltext)
    datax = data["data_values"]

    file = open("stock_data/" + symbol + ".csv", "a")

    for point in datax:
        if point[0] > last_line_data:
           file.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
    file.close()

