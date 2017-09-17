import math
from gaussian import Gaussian
from random import uniform
import numpy as np


class GaussianMixture:

    def __init__(self, data, n_mix, sigma_min=0.1, sigma_max=1.0):
        self.data = data

        mu_min = min(data)
        mu_max = max(data)

        # create n-gaussians that will comprise the gaussian mixture model
        self.gaussians = {}
        # probability of each gaussians
        self.mix = {}
        # number of gaussians
        self.n_mix = n_mix
        # initialize the gaussians
        for i in range(0, n_mix):
            self.gaussians[i] = Gaussian(uniform(mu_min, mu_max),
                                    uniform(sigma_min, sigma_max))
            self.mix[i] = 1/n_mix

    def estimate(self):
        self.loglike = 0.

        # probability that datum is a member of gaussian component k
        wp = np.zeros((len(self.data), self.n_mix), dtype=np.float64)

        for k in range(0, self.n_mix):
            wp[:, k] = self.gaussians[k].pdf(self.data)*self.mix[k]

        den = np.sum(wp, axis=1, dtype=np.float64)
        deng = np.ones_like(wp)

        for k in range(0, self.n_mix):
            deng[:, k] = den

        # normalize probability
        wp = np.divide(wp, deng)
        self.loglike = np.log(np.sum(wp, axis=0))
        return wp

    def maximize(self, weights):
        (left, right) = zip(*weights)


    def iterate(self):
        # iterate

