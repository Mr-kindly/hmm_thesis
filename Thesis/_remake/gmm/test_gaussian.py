from gaussian import Gaussian


x = Gaussian(mu=0., sigma=1.)
print (x)

x.update(mu=2., sigma=3.)
print x.pdf([2, 3, 4, 5])
print (x)


# g = Gaussian(mu=2, sigma=3)
# print(g.pdf(2))
# # g.update(mu=1, sigma=2)
# # print(g.pdf(6))
#
# mdl = {}
# for i in range(0, 3):
#     mdl[i] = Gaussian(mu=1 + i, sigma=2)
#
# print(mdl[0].pdf(1))
# print(mdl[1].pdf(1))
# print(mdl[2].pdf(1))