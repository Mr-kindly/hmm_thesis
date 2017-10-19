import data_get
import time
import datetime
import numpy as np
import pandas as pd

start = int(time.time()) - 86400 * 35
end = int(time.time()) - 86400 * 5

start_date =  datetime.datetime.fromtimestamp(start).date()
end_date = datetime.datetime.fromtimestamp(end).date()

daterange = pd.date_range(start=start_date, end=end_date)
x = data_get.data_get2(symbol='AC')
data_json = x.latency_range(t_from=start, t_end=end)
print data_json
data = np.column_stack([data_json["o"], data_json["l"], data_json["h"], data_json["c"]])

df = pd.DataFrame(data=data, index=data_json["t"], columns=["Open", "Low", "High", "Close"])
df.index.title = "Date"

df.to_csv("data_actual_"+str(start)+"_"+str(end)+".csv")
