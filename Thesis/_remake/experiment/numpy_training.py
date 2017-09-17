import numpy as np


z = np.array([[1, 2, 3, 4], [4, 2, 1, 1], [1, 3, 4, 4], [-1, 0, 2, 3]], dtype=np.float64)

# zsum = np.sum(z,axis=1)
# print zsum
#
# deng = np.ones_like(z)
#
# for i in range(0, 4):
#     deng[:, i] = zsum
#
# print deng
#
# z_norm = np.divide(z, deng)
#
# print z_norm

s = np.linalg.inv(z)
ss = np.matmul(s,z)
ss2 = np.linalg.det(z)
print ss2