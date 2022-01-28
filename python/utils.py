import numpy as np

class SecInstanceArray():
    def __init__(self, values, colors, types=None):
        self.value = values
        self.color = colors
        if types is not None:
            self.type = types
        else:
            self.type = np.zeros(len(values), dtype=int)
            
    def __getitem__(self, key):
        return SecretaryInstance(self.value[key], self.color[key], self.type[key])

    def __len__(self):
        return len(self.value)

class SecretaryInstance():
    """docstring for SecretaryInstance."""

    def __init__(self, value, color, type=0):
        super(SecretaryInstance, self).__init__()
        self.value = value
        self.color = color
        self.type = type

    def __str__(self):
        return f"Value: {self.value}, Color: {self.color}, Type: {self.type}"

def GetThreshold(p):
    t = len(p) * [0]
    k = len(p)
    t[k - 1] = (1 - (k - 1) * p[k - 1]) ** (1 / (k - 1))
    
    for i in range(k - 2, 0, -1):
        sum = 0

        for r in range(i + 1):
            sum += p[r]

        sum /= i

        t[i] = t[i + 1] * (((sum - p[i]) / (sum - p[i + 1])) ** (1 / i))

    t[0] = t[1] * np.exp(p[1] / p[0] - 1)
    return t

def ComputeThreshold(max_size):
    t = (max_size + 1) * [0]

    for i in range(1, max_size):

        p = (i + 1) * [1.0 / (i + 1)]
        t[i + 1] = GetThreshold(p)[0]

    return t