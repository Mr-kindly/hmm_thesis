from sklearn.externals import joblib
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required = True,
	help = "Ticker symbol for stocks")
args = vars(ap.parse_args())
symbol = str(args["symbol"])
symbol.strip()
print (symbol)


# load HMM-generated

try:
    model = joblib.load(symbol+'_hmm2.pkl')
except IOError:
    print("Model not generated yet.")
    exit(1)

print("Transition matrix")
print(model.transmat_)
print("Means and vars of each hidden state")
for i in range(model.n_components):
    print "{0}th hidden state".format(i)
    print "mean = ", model.means_[i]
    print "var = ", np.diag(model.covars_[i])


price_sample = np.array([867.00, 863.00, 868.00, 855.00], dtype=float)
price_actual = np.array([860, 866, 870, 860], dtype=float)
data = np.column_stack([0.0164, -0.01371, -0.008, 0.0023])
# data2 = np.column_stack([])
hidden_state = model.predict(data)
print (hidden_state)

state_emit = np.array(model.means_[hidden_state], dtype=float)
prediction = np.dot(state_emit, price_sample) + price_sample
print (state_emit)
print ("Results: ")
print ("==========================================================")
print ('CLOSE   OPEN    HIGH    LOW')
print ("==========================================================")
print ("Prediction")
print (prediction)
print ("Actual")
print price_actual
print ("Percent error")
print np.divide(np.subtract(prediction, price_actual), price_actual)
