from utils import SecretaryInstance
import numpy as np

def ComputeSolution(elements, distributions, q):
    sum_arr = np.cumsum(q)
    sum_arr = np.insert(sum_arr, 0, 0.0)[:-1]
    x = 1 - (q / (2 - sum_arr))
    mask = np.zeros(len(elements))
    mask[elements.type == 0] = distributions[0].Reverse(x[elements.type == 0])
    mask[elements.type == 1] = distributions[1].Reverse(x[elements.type == 1])
    cond = elements.value >= mask
    result = np.where(cond == True)
    if np.sum(result) > 0:

        return elements[result[0][0]]

    return SecretaryInstance(-1, -1)

# IID
def ComputeSolutionIID(elements, distributions, q):
    p = (2 / 3) / len(elements)
        
    x = 1 - p / (1 - p * np.arange(len(elements)))
    mask = np.zeros(len(elements))
    mask[elements.type == 0] = distributions[0].Reverse(x[elements.type == 0])
    mask[elements.type == 1] = distributions[1].Reverse(x[elements.type == 1])
    cond = elements.value >= mask
    result = np.where(cond == True)
    if np.sum(result) > 0:
        
        return elements[result[0][0]]
    
    return SecretaryInstance(-1, -1)