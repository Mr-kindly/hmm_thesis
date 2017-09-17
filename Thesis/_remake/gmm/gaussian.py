import math
import numpy as np


class Gaussian:

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, data):
        data = np.array(data, dtype=np.float64)
        z = (data - self.mu)/self.sigma
        y = (1/(self.sigma * np.sqrt(2.0*np.pi))) * np.exp(-z**2/2.0)
        return y

    def pdf_scalar(self, data):
        z = (float(data) - self.mu)/self.sigma
        y = (1/(self.sigma * math.sqrt(2.0*math.pi))) * math.exp(-z**2/2.0)
        return y

    def update(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def __repr__(self):
        return 'GaussianObject({0:4.6},{1:4.6})'.format(self.mu, self.sigma)
