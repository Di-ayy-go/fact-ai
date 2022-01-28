import sys
import numpy as np
from utils import SecretaryInstance, SecInstanceArray
from random_handler import RandomHandler

rh = RandomHandler(432)
def GetSecretaryInput(sizes: list, prob = []):
    num_colors = len(sizes)
    instance = []
    rand = 2.0
    if len(prob) >  0:
        rand = rh.eng() / 1e16  

    for i in range(len(sizes)):

        for j in range(sizes[i]):
            instance.append(SecretaryInstance(rh.eng() / 10, i))

        if len(prob) > 0:

            if prob[i] > rand and rand >= 0:
                instance[len(instance) - 1].value = sys.maxsize

            rand -= prob[i]

    return instance


def GetProphetInput(size: int, dist):
    num_colors = size
    instance = []
    dist_0 = dist[0].Sample(size // 2)
    dist_1 = dist[1].Sample(size // 2)
    dists = np.array([dist_0, dist_1]).flatten()
    types = np.array([np.zeros(size // 2, dtype=int), np.ones(size // 2, dtype=int)]).flatten()
    instance = SecInstanceArray(dists, np.arange(size), types)
    return instance