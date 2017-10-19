import pandas as pd
from cvxopt import *
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-sl', '--symbols', required=True, help='path to txt file that contains the list of symbols to be considered')
args = vars(ap.parse_args())

path = args["symbols"]

# load text file of symbols to be considered
with open(path, 'r') as listSymbols:
    slist = listSymbols.read()
    slist = slist.split("\n")
    listSymbols.close()


# read and register all closing price of the listed
df_list = pd.DataFrame()


for symbol in slist:
    df = pd.read_csv("../training/"+symbol+".csv")
    p_close = df["Price"].reindex(index=df.index[::-1]).rename(columns={"Price":symbol})
    df_list[symbol] = p_close

# calculate covariance
cov = df_list.cov(min_periods=None)

# average returns
mean = df_list.mean()
print mean

# goal
expected_return = 0.1

ss = cov.as_matrix()
n = len(slist)

# Define QP params
sigma = matrix(ss)
ave_ret = matrix(mean.as_matrix())
q = matrix(np.zeros([n, 1]))


G = matrix(np.concatenate(np.transpose(np.array(mean.as_matrix)), np.identity(n)), 0)
h = matrix(np.concatenate((
              np.ones(([1, 1]))*expected_return,
              np.zeros(([n, 1]))), 0))

A = matrix(1.0, (1, n))
b = matrix(1.0)

sol = solvers.qp(sigma, q, G, h, A, b)

print sol