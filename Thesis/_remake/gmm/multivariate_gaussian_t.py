import multivariate_gaussian
import numpy as np

mu = np.array([1, 2, 3])
covar = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
x = multivariate_gaussian.GaussianMultivariate(mu, covar)

data_test = np.array([[2, 2, 2], [2, 3, 4], [1, 1, 1]])
proba = x.pdf(data_test)
print proba
print x

# test for univariate
mu = np.array([0])
covar = np.array([1])
y = multivariate_gaussian.GaussianUnivariate(mu, covar)

data_test2 = np.array([1.0])

proba2 = y.pdf(data_test2)
print proba2
print y