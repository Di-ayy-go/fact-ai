import sys
from utils import SecretaryInstance
from random_handler import RandomHandler
from distributions import RandomDistribution

rh = RandomHandler()
def GetSecretaryInput(sizes: list, prob = []):
    """
    """
    num_colors = len(sizes)
    instance = []
    rand = 2.0
    if len(prob) >  0:
        rand = rh.eng() / 1e16
        print(rand)

    for i in range(len(sizes)):

        for j in range(i):
            instance.append(SecretaryInstance(rh.eng() / 10, i))
        if len(prob) > 0:

            if prob[i] > rand and rand >= 0:
                instance[len(instance) - 1].value = float('inf')

        rand -= prob[i]

    return instance


def GetProphetInput(size: int, dist: RandomDistribution):
    """
    """
    num_colors = size
    instance = []
    for i in range(size):

        if i < size / 2:
            instance.append(SecretaryInstance(dist.r(0)), i, 0)

        else:
            instance.append(SecretaryInstance(dist.r(1)), i, 0)

    return instance
