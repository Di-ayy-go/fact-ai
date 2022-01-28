import numpy as np

class RandomHandler(object):
    """docstring for RandomHandler."""

    def __init__(self, seed):
        super(RandomHandler, self).__init__()
        self.seed = seed
        # self.rg = np.random.Generator(np.random.MT19937(self.seed))
        self.rg = np.random.default_rng(self.seed)
        print(f"RH Init {seed}, {self.rg.random()}, {self.rg.random()}")

    def eng(self):
        return int(self.rg.random() * 1e16)

if __name__ == '__main__':
    rg = RandomHandler()
    print(rg.eng())
