from cvxopt import solvers, matrix
import numpy as np
import matplotlib.pyplot as plt


cov_raw = open('csv_qp/Covariance.csv')
mean_raw = open('csv_qp/mean_return.csv')
std_raw = open('csv_qp/stdDev_return.csv')


cov_lin = cov_raw.readlines()
mean_lin = mean_raw.readlines()
std_lin = std_raw.readlines()


x = np.zeros(1000, dtype=float)

x = cov_lin[1].split(',')
