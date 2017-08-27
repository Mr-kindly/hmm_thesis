import numpy as np


data_raw = np.array([1.0, 2.0, 4.0, 6.0, 4.0, 2.0, 3.0, 4.0, 5.0, 3.0, 2.0, 3.0, 4.0, 5.0, 1.0, 4.0, 5.0, 6.0, 7.0, 8.0,])

print data_raw


data_length = len(data_raw)

#print data_length
#print data_raw[1]

data = np.zeros([17,3], dtype=np.float32)

for i in range(0, 17):
    data[i] = data_raw[0+i:3+i]

data = data.T
print data