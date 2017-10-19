from sklearn.externals import joblib
import argparse
import numpy as np


# ap = argparse.ArgumentParser()
# ap.add_argument("-s", "--symbol", required = False,
# 	help = "Ticker symbol for stocks")
# args = vars(ap.parse_args())
# symbol = str(args["symbol"])
# symbol.strip()
# print (symbol)


# load HMM-generated
title = str('AC_hmm2.pkl')
print("Accessing: " + title)

try:
    model = joblib.load(title)
except IOError:
    print("Model not generated yet.")
    exit(1)

print("Transition matrix")
print(model.transmat_)
print("Means")
print(model.means_)
print("Covariance")
print(model.covars_)


price_sample = np.array([867.00, 863.00, 868.00, 855.00], dtype=float)
price_actual = np.array([860, 866, 870, 860], dtype=float)


data = np.column_stack([[0.0164, -0.01371, -0.008, 0.0023]])
print(data)

# data2 = np.column_stack([])
# hidden_state = model.predict(data)
log_proba = model.score(data)
# print (hidden_state)
print (log_proba)

