import data_get
import numpy as np

x = data_get.data_get2(symbol='AC')
data = x.load()

datax = data["o"]
print(datax)

data_latency_0 = np.column_stack([data["o"], data["l"], data["h"], data["c"]])

data_latency = np.diff(data_latency_0, axis=0)
data_latency = np.divide(data_latency, np.delete(data_latency_0, -1, axis=0))
print (data_latency)

try:
    pred_data = np.load("grid_cache/test_grid.npy")

except IOError:
    pred_open = np.linspace(-0.1, 0.1, 50)
    pred_low = np.linspace(0., 0.1, 10)
    pred_max = np.linspace(0., 0.1, 10)
    pred_close = np.linspace(-0.1, 0.1, 50)

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
    np.save("grid_cache/test_grid.npy",pred_data)

print(pred_data[56,0:4])
# pred_data = np.column_stack([pred_open, pred_low, pred_max, pred_close])
# print (np.size(np.column_stack(pred_data[1, 0:4]), axis=0))
# datax = np.append(data_latency, np.column_stack(pred_data[1, 0:4]), axis=0)
# print(datax)


# for i in pred_data[:, 0:4]:
#     print(data_latency)
#     print(i)
#     datax = np.append(arr=data_latency, values=i, axis=0)
#     print (datax)