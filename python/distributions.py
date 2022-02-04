import numpy as np
from random_handler import RandomHandler
import scipy.stats as sc

class UniformDistribution(sc.distributions.rv_frozen):
    """
    Wrapper for Scipy uniform distribution.
    Contains additional methods needed to reproduce results of paper.
    
    args:
        loc (int): mean of distribution
        scale (int): range/standard deviation of distribution
        n (int): number of samples to be generated 
        (placeholder to make this class interchangable with BinomialDistribution)
    """

    def __init__(self, loc, scale, n):
        super(UniformDistribution, self).__init__(sc.uniform, loc, scale)
        self.loc = loc
        self.scale = scale

        p_th = np.zeros(n)
        V = np.zeros(n)

        V[n - 1] = scale / 2
        for i in range(n - 2, -1, -1):
            p_th[i] = V[i + 1]
            V[i] = (scale + p_th[i]) / 2

        self.p_th = p_th
        self.V = V

    def PThreshold(self, index):
        """
        Returns PThreshold value at index `index`

        args:
            index (int/list): indices to be retrieved
        """
        return self.p_th[index]

    def Sample(self, size):
        """
        Wrapper for rvs sampling method for code clarity
        and consistency with original C++ codebase

        args:
            size (int): number of samples to be generated
        """
        return self.rvs(size=size)

    def Middle(self, n):
        """
        Computes middle value of distribution using `n` values.

        args:
            n (int): number of values to consider to calculate middle.
        """
        return self.scale * (1 / 2) ** (1 / n)

    def Reverse(self, x):
        """
        Returns 
        """
        return x * self.scale


class BinomialDistribution(sc.distributions.rv_frozen):
    """
    Wrapper for Scipy binomial distribution.
    Contains additional methods needed to reproduce results of paper.
    
    args:
        n (int): number of independent experiments
        p (int): probability of success of Bernoulli trial
    """

    def __init__(self, n, p):
        super(BinomialDistribution, self).__init__(sc.binom, n, p)
        self.n = n
        n = n + 1
        choose = np.zeros((n, n))
        probability = np.ones(n)
        r_probability = np.ones(n)

        choose[:, 0] = 1

        for i in range(1, n):
            for j in range(1, n):
                choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j]

        for i in range(1, n):
            probability[i] = probability[i - 1] * p
            r_probability[i] = r_probability[i - 1] * (1 - p)

        self.choose = choose
        self.probability = probability
        self.r_probability = r_probability
        self._ComputeMaxDist(n)

    def Expected(self, lower_bound):
        """
        Calculates expected value using lower bound.
        Based on implementation in C++ repo.

        args:
            lower_bound (int): lower bound of expected value
        """
        ans = 0
        rang = 0
        n = len(self.probability) - 1
        i = int(np.ceil(lower_bound * n))
        while i <= n:
            ans += self.probability[i] * self.r_probability[n - i] * self.choose[n][i] * i / n;
            rang += self.probability[i] * self.r_probability[n - i] * self.choose[n][i];
            i += 1
    
        return ans / rang

    def Reverse(self, x):
        """
        Computes reverse of x using numpy arrays for efficiency
        """
        a = np.cumsum(self.choose[self.n] * self.probability * self.r_probability[::-1])
        c = x - a[..., None]
        result = np.argmax(c <= 0, axis=0) / self.n
        result[result == 0] = 1
        return result

    def Sample(self, size):
        """
        Wrapper for rvs sampling method for code clarity
        and consistency with original C++ codebase

        args:
            size (int): number of samples to be generated
        """
        rand = np.random.uniform(size=size)
        return (self.rvs(size=size) + rand) / len(self.probability)

    def Middle(self, n):
        """
        n is passed because for compatibility. It used in UniformDistribution.
        """
        for i in range(len(self.max_dist) - 1, -1, -1):
            if self.max_dist[i] >= 0.5:
                return i / (len(self.max_dist) - 1)

        return 0

    def _ComputeMaxDist(self, num_dists):
        """
        Internal method for computing max_dist array.
        """
        max_dist = np.zeros(len(self.probability))
        x = 0
        n = self.n
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
        self.p_th = p_th
        self.max_dist = max_dist

    def PThreshold(self, index):
        return self.p_th[index]
