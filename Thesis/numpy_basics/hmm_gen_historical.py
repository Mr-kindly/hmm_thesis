from sklearn.externals import joblib
import numpy as np
from matplotlib import cm, pyplot as plt
import hmmlearn.hmm as hmm
import argparse


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
    file = open('hist_stock_data/'+symbol+'_hist.csv')

except:
    print("FILE NOT FOUND or symbol not found")
    exit(1)


linelist = file.readlines()
p_open = np.zeros(len(linelist) - 2, dtype=float)
p_close = np.zeros(len(linelist) - 2, dtype=float)
p_high = np.zeros(len(linelist) - 2, dtype=float)
p_low = np.zeros(len(linelist) - 2, dtype=float)
volume = np.zeros(len(linelist)-2, dtype=float)
i = 0
k = 0

for x in linelist:
    y = x.split(',')
    try:
        p_close[i] = float(y[1])
        p_open[i] = float(y[2])
        p_high[i] = float(y[3])
        p_low[i] = float(y[4])
    except ValueError:
        continue
    i = i + 1

###############################################################################
# Data pre-processing
# percent change approach

p_close = p_close[::-1]
p_open = p_open[::-1]
p_high = p_high[::-1]
p_low = p_low[::-1]


diff_close = np.diff(p_close)
diff_open = np.diff(p_open)
diff_high = np.diff(p_high)
diff_low = np.diff(p_low)

v_close = np.divide(diff_close[1:], p_close[:len(p_close)-2])
v_open = np.divide(diff_open[1:], p_open[:len(p_open)-2])
v_high = np.divide(diff_high[1:], p_high[:len(p_high)-2])
v_low = np.divide(diff_low[1:], p_low[:len(p_low)-2])

X = np.column_stack([v_close, v_open, v_high, v_low])

###############################################################################
# Run Gaussian HMM

# Make an HMM instance and execute fit
model = hmm.GaussianHMM(n_components=4, covariance_type="diag", n_iter=1000).fit(X)

# Store the model
joblib.dump(model, symbol+'_hmm2.pkl')


###############################################################################
# Print trained parameters and plot
print("Transition matrix")
print(model.transmat_)
print("Means and vars of each hidden state")
for i in range(model.n_components):
    print "{0}th hidden state".format(i)
    print "mean = ", model.means_[i]
    print "var = ", np.diag(model.covars_[i])

print('\nHMM generated!\n')


plt.plot(p_close)
plt.plot(p_open)
plt.plot(p_high, '-')
plt.plot(p_low, '--')
plt.ylim([min(p_low) - 10, max(p_high) + 10])
plt.xlim([0, len(p_close)])
plt.title('Historical Stock Prices for Ayala Corporation')
plt.ylabel('Price (Php)')
plt.show()

#plt.plot(hidden_states)
#plt.show()

