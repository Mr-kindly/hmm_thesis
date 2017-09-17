import numpy as np


class GaussianMultivariate:
    def __init__(self, mu, covar):
        # initialize a multivariate gaussian.
        '''
        :param mu: length d vector which represent the means of the data
        :param covar: a d x d matrix which represents the covariance between the data
        '''

        self.mu = mu
        self.covar = covar
        self.length_mu = len(mu)

    def pdf(self, data):

        '''
        
        :param data: the data to which the probability will be computed
        :return: scalar,
        '''

        z1 = np.subtract(data, self.mu)
        z2 = np.linalg.inv(self.covar)
        z = np.matmul(np.matmul(z1, z2), z1.T)
        det_covar = np.linalg.det(self.covar)
        const = 1/np.sqrt(np.multiply(np.power((2*np.pi), self.length_mu), det_covar))
        proba = const * np.exp(-z/2)
        proba2 = np.diag(proba).T
        return proba2

    def __str__(self):
        str = "means = \n{0}\n".format(self.mu)
        str2  = "covars = \n{0}".format(self.covar)
        return str + str2

class GaussianUnivariate:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, data):
        z = np.divide(np.subtract(data, self.mu), self.sigma)
        const = 1/((2*np.pi)*self.sigma)
        y = np.multiply(const, np.exp(-(1/2) * np.power(z, 2)))
        return y

    def __str__(self):
        return "UnivariateGaussian( mean = {0}, S.D. = {1} )".format(self.mu, self.sigma)

