import numpy as np
import multivariate_gaussian
from random import uniform

class GaussianMixture:

    def __init__(self, data, mu, covar, n_mix):
        self.data = data
        self.mu = mu
        self.covar = covar

        self.n_mix = n_mix
        self.weights = 1/n_mix

        mu_min = min(data)
        mu_max = max(data)

        for i in range(0, n_mix):
            Gaussians = multivariate_gaussian.GaussianMultivariate(
                uniform(mu_min, mu_max),
                uniform()
            )

    def Estep(self):
        posterior =