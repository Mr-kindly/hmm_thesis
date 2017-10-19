from sklearn.externals import joblib
import numpy as np
import argparse
import data_get
import datetime
import time
import pandas as pd


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", help="ticker symbol for stocks of a company", required=True)
ap.add_argument("-t", "--time", help="number days from today", required=True)
args = vars(ap.parse_args())

symbol = str(args["symbol"])
days = int(str(args["time"]))
title = "models/"+symbol + "_hmm.pkl"

try:
    model = joblib.load(title)

except IOError:
    print("Model not generated yet")
    exit(1)


# Perform estimation over these values
try:
    pred_data = np.load("grid_cache/test_grid.npy")

except IOError:
    pred_open = np.linspace(-0.05, 0.05, 10)
    pred_low = np.linspace(0, 0.05, 10)
    pred_max = np.linspace(0, 0.05, 10)
    pred_close = np.linspace(-0.05, 0.05, 10)

    open_x = []
    low_x = []
    max_x = []
    close_x = []

    for h in pred_open:
        for i in pred_low:
            for j in pred_max:
                for k in pred_close:
                    open_x = np.append(open_x, h)
                    low_x = np.append(low_x, i)
                    max_x = np.append(max_x, j)
                    close_x = np.append(close_x, k)
    pred_data = np.column_stack([open_x, low_x, max_x, close_x])
    np.save("grid_cache/test_grid.npy", pred_data)


# Load Data
data_src = data_get.data_get2(symbol=symbol)
# data_json = data_src.load()
x = int(time.time()) - 86400*days
data_json = data_src.latency_range(x - 86400 * 14, x)
data_latency = np.column_stack([data_json["o"], data_json["l"], data_json["h"], data_json["c"]])

# Normalization
data_latency_norm = np.diff(data_latency, axis=0)
data_latency_norm = np.divide(data_latency_norm, np.delete(data_latency, -1, axis=0))

# Calculate most probable data sequence
loglik = []
datax= np.array([0., 0., 0., 0.])
for i in pred_data[:, 0:4]:
    data = np.append(data_latency_norm, np.column_stack(i), axis=0)
    loglik = np.append(loglik, model.score(data))

alpha = np.argmax(loglik)
print(alpha)
last_data = data_latency[-1, 0:4]
predict = pred_data[alpha, 0:4]
print(predict)

# Post Processing
price_delta = np.multiply(predict, last_data)
print(price_delta)
price_predict = np.add(price_delta, last_data)
print(price_predict)

# Save Prediction
tstamp = datetime.datetime.fromtimestamp(x)
tstamp_str = str(tstamp.date())
title_pred = "predictions/p_" + "range_" + tstamp_str + ".csv"
np.savetxt(title_pred, price_predict, delimiter=",")

