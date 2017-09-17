import json
import urllib
import datetime as dt

class DataAcquire:

    def __init__(self, stocks_text_file):
        self.symbols = open(stocks_text_file).read()
        self.symbols = self.symbols.split('\n')

    def read_json(self, symbol):
        htmltext = urllib.urlopen("https://www.bloomberg.com/markets/chart/data/1D/"+symbol+":PM")
                    # https://www.bloomberg.com/markets/watchlist/recent-ticker/DD:PM
        data = json.load(htmltext)
        datax = data["data_values"]
        return datax

    def generate(self):

        for symbol in self.symbols:
            datax = self.read_json(symbol=symbol)

            try:
                file = open("stock_data/" + symbol + ".csv", "r")
                linelist = file.readlines()
                file.close()
                last_line = linelist[-1]
                last_line_array = last_line.split(',')
                last_line_data = last_line_array[0]

                st = dt.datetime.fromtimestamp(float(last_line_data)/1000).strftime('%Y-%m-%d %H:%M:%S')
                str = "Last Updated: " + st
                print str

                for datum in datax:
                    if datum[0] > last_line_data:
                        file.write('{0}, {1}\n'.format(datum[0], datum[1]))
                file.close()

            except IndexError or IOError:
                file = open("stock_data/" + symbol + ".csv", "w")
                for datum in datax:
                    file.write('{0}, {1}\n'.format(datum[0], datum[1]))
                file.close()
