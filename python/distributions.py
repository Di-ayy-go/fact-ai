import numpy as np
from random_handler import RandomHandler

class RandomDistribution(object):
    """docstring for RandomDistribution."""

    def __init__(self, distributions: list):
        self.generator = RandomHandler().rg
        self.distributions = distributions

    def __getitem__(self, key):
        return self.distributions[key]

    def r(self, key):
        method = self.distributions[key]
        return self.generator.method

if __name__ == '__main__':
    rd = RandomDistribution(['uniform'])
    print(rd.r(0))
