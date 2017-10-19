from sklearn.externals import joblib
import numpy as np
import hmmlearn.hmm as hmm
import argparse
import pandas as pd


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required = True,
	help = "Ticker symbol for stocks")
args = vars(ap.parse_args())

symbol = str(args["symbol"])
symbol.strip()
print (symbol)
###############################################################################
# Data acquisition
try:
    # file = open('hist_stock_data/'+symbol+'_hist.csv')
    # file = open('hist_stock_data/AC_hist.csv')
    df = pd.read_csv('../training/AGI.csv')
except IOError:
    print("FILE NOT FOUND or symbol not found")
    exit(1)

p_close = df["Price"].reindex(index=df.index[::-1])
p_open = df["Open"].reindex(index=df.index[::-1])
p_high = df["High"].reindex(index=df.index[::-1])
p_low = df["Low"].reindex(index=df.index[::-1])


###############################################################################
# Data pre-processing
# percent change approach

diff_close = np.diff(p_close)
diff_open = np.diff(p_open)
diff_high = np.diff(p_high)
diff_low = np.diff(p_low)

v_close = np.divide(diff_close[1:], p_close[:len(p_close)-2])
v_open = np.divide(diff_open[1:], p_open[:len(p_open)-2])
v_high = np.divide(diff_high[1:], p_high[:len(p_high)-2])
v_low = np.divide(diff_low[1:], p_low[:len(p_low)-2])

X = np.column_stack([v_open, v_low, v_high, v_close])

###############################################################################
# Run Gaussian HMM

# Make an HMM instance and execute fit
model = hmm.GMMHMM(n_components=5, n_mix=4, covariance_type="full", n_iter=10000, verbose=False).fit(X)

# Store the model
joblib.dump(model, "./models/"+symbol+'_hmm.pkl')


###############################################################################

print('\nHMM generated!\n')