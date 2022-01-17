import numpy as np

class RandomHandler(object):
    """docstring for RandomHandler."""

    def __init__(self):
        super(RandomHandler, self).__init__()
        self.seed = np.random.randint(0, 1e6, size=1)[0]
        self.rg = np.random.Generator(np.random.MT19937(self.seed))

    def eng(self):
        return int(self.rg.random() * 1e16)

if __name__ == '__main__':
    rg = RandomHandler()
    print(rg.eng())
