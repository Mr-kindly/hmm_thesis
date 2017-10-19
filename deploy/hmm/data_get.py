import requests
import json
import time
import datetime

class data_get2:

    def __init__(self, symbol):
        self.symbol = symbol

    def load(self, latency=14, mode='latency'):

        self.latency_length(length=latency)
        url = "http://api.pse.tools/api/chart/history?"

        settings = {

            "symbol": self.symbol,
            "resolution": "D",
            "from": str(self.t_from),
            "to": str(self.t_end)
        }

        response = requests.get(url, settings)
        data = json.loads(response.text)

        return data

    # latency length defaulted to 2 weeks
    def latency_length(self, length):

        x = int(time.time())
        self.t_end = x
        self.t_from = x - 86400*length
        return 0

    # date define
    def latency_range(self, t_from, t_end):

        self.t_end = t_end
        self.t_from = t_from

        url = "http://api.pse.tools/api/chart/history?"

        settings = {

            "symbol": self.symbol,
            "resolution": "D",
            "from": str(self.t_from),
            "to": str(self.t_end)
        }

        response = requests.get(url, settings)
        data = json.loads(response.text)

        return data