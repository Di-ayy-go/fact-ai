import numpy as np

class RandomHandler(object):
    """docstring for RandomHandler."""

    def __init__(self, seed=1223):
        super(RandomHandler, self).__init__()
        self.seed = seed
        self.rg = np.random.Generator(np.random.MT19937(seed))

    def eng(self):
        return int(self.rg.random() * 1e16)

if __name__ == '__main__':
    rg = RandomHandler()
    print(rg.eng())
