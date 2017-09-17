from __future__ import print_function

import datetime

import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator

try:
    from matplotlib.finance import quotes_historical_yahoo_ochl
except ImportError:
    # For Matplotlib prior to 1.5.
    from matplotlib.finance import (
        quotes_historical_yahoo as quotes_historical_yahoo_ochl
    )

from hmmlearn.hmm import GMMHMM


print(__doc__)

###############################################################################
# Data Acquisition

X = np.column_stack([[0.1, 0.2, 0.3, 0.1], [0.3, 0.4, 0.7, 0.1], [0.1, 0.2, 0.3, 0.5], [0.5, 0.6, 0.3, 0.5], [0.1, 0.3, 0.3, 0.3]])


###############################################################################
# Run Gaussian HMM
print("fitting to HMM and decoding ...", end="")

# Make an HMM instance and execute fit
model = GMMHMM(n_components=4, n_mix=4, covariance_type="diag", n_iter=1000).fit(X)

# Predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)
print(hidden_states)
print("done")

###############################################################################
# Print trained parameters and plot
print("Transition matrix")
print(model.transmat_)
print()


print("Means and vars of each hidden state")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("var = ", np.diag(model.covars_[i]))
    print()




# fig, axs = plt.subplots(model.n_components, sharex=True, sharey=True)
# colours = cm.rainbow(np.linspace(0, 1, model.n_components))
# for i, (ax, colour) in enumerate(zip(axs, colours)):
#     # Use fancy indexing to plot data in each state.
#     mask = hidden_states == i
#     ax.plot_date(dates[mask], close_v[mask], ".-", c=colour)
#     ax.set_title("{0}th hidden state".format(i))
#
#     # Format the ticks.
#     ax.xaxis.set_major_locator(YearLocator())
#     ax.xaxis.set_minor_locator(MonthLocator())
#

#     ax.grid(True)
#
# plt.show()
#