import numpy as np

class RandomHandler(object):
    """RNG class used for consistency across experiments."""

    def __init__(self, seed=42):
        super(RandomHandler, self).__init__()
        self.seed = seed
        self.rg = np.random.default_rng(self.seed)
        print(f"RH Init with seed {seed}. Samples: {self.rg.random()}, {self.rg.random()}")

    def eng(self):
        return int(self.rg.random() * 1e16)

if __name__ == '__main__':
    rg = RandomHandler()
    print(rg.eng())
