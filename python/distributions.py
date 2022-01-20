import numpy as np
from random_handler import RandomHandler
import scipy.stats as sc

class RandomDistribution(object):
    """docstring for RandomDistribution."""

    def __init__(self, distributions: list, params: list):
        self.distributions = distributions
        self.params = params

    def __getitem__(self, key):
        return self.distributions[key]


class UniformDistribution(sc.distributions.rv_frozen):
    """docstring for UniformDistribution."""

    def __init__(self, loc, scale, n):
        super(UniformDistributions, self).__init__(sc.uniform, loc, scale)
        self.loc = loc
        self.scale = scale
        self.n = n

        p_th_ = n * [0]
        V = n * [0]

        V[n - 1] = scale / 2
        for i in range(n - 2, -1, -1):
            p_th_[i] = V[i + 1]
            V[i] = (scale + p_th_[i]) / 2

        self.p_th_ = p_th_
        self.V = V

    def PThreshold(self, index):
        return self.p_th_[index]

    def Sample(self):
        return self.rvs()

    def Middle(self, n):
        return self.scale * (1 / 2) * (1 / n)

    def Reverse(self, x):
        return x * self.scale


class BinomialDistribution(sc.distributions.rv_frozen):
    """docstring for BinomialDistribution."""

    def __init__(self, n, p):
        super(BinomialDistribution, self).__init__(sc.binom, n, p)
        self.n = n
        n = n + 1
        choose = np.zeros(n, n)
        probability = np.ones(n)
        r_probability = np.ones(n)

        for i in range(n):
            choose[i][0] = 1

        for i in range(1, n):
            choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j]

        for i in range(n):
            probability[i] = probability[i - 1] * p
            r_probability[i] = r_probability[i - 1] * (1 - p)

        self.choose = choose
        self.probability = probability
        self.r_probability = r_probability
        ComputeMaxDist(n)

    def Expected(self, lower_bound):
        return self.expect(lb=lower_bound)

    def Reverse(x):
        for i in range(self.n + 1):
            x -= self.choose[self.n][i] * self.probability[i] * self.r_probability[self.n - i]

            if x <= 0:
                return i / n

        return 1

    def Sample(self):
        return self.rvs()

    def Middle(self, n):
        for i in range(len(self.max_dist), -1, -1):
            if self.max_dist[i] >= 0.5:
                return i / (len(self.max_dist) - 1)

        return 0

    def ComputeMaxDist(num_dists):
        max_dist = np.zeros(len(self.probability))
        x = 0
        for i in range(n, -1, -1):
            x += self.choose[n][i] * self.probability[i] * self.r_probability[n - i]
            max_dist[i] = 1 - (1 - x) ** num_dists

        # Computing PThreshold
        V, p_th = np.zeros(num_dists), np.zeros(num_dists)
        V[num_dists - 1] = self.Expected(0)
        for i in range(num_dists - 2, -1, -1):
            p_th[i] = V[i + 1]
            V[i] = self.Expected(p_th[i])

        self.V = V
        self.p_th = self.p_th
        self.max_dist = max_dist
