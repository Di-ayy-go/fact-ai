import sys
from utils import SecretaryInstance
from random_handler import RandomHandler

rh = RandomHandler()
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


# def GetProphetInput(size: int, dist):
#     """
#     """
#     num_colors = size
#     instance = []
#     dist_0 = dist[0].Sample(size // 2)
#     dist_1 = dist[1].Sample(size // 2)
#     for i in range(size // 2):
#         instance.append(SecretaryInstance(dist_0[i], i, 0))
    
#     for i in range(size // 2):
#         instance.append(SecretaryInstance(dist_1[i], i + size // 2, 0))

#     return instance



def GetProphetInput(size: int, dist):
    """
    """
    num_colors = size
    instance = []
    for i in range(size):

        if i < size / 2:
            instance.append(SecretaryInstance(value=dist[0].Sample(1), color=i, type=0))

        else:
            instance.append(SecretaryInstance(value=dist[1].Sample(1), color=i, type=1))

    return instance