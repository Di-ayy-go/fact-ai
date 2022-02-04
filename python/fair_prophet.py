from utils import SecretaryInstance, filterElements
import numpy as np

def ComputeSolution(elements, distributions, q):
    """
    This function implements the proposed algorithm to achieve
    fairness in the general distributions case.

    args:
        elements (SecInstanceArray): array containing instances
        distributions (list): list containing arrival order distributions
        q (list): offline fair optimal algorithm selection probabilities 

    returns:
        best candidate object   
    """
    sum_arr = np.cumsum(q)
    sum_arr = np.insert(sum_arr, 0, 0.0)[:-1]
    condition = 1 - (q / (2 - sum_arr))
    return filterElements(elements, distributions, condition)

def ComputeSolutionIID(elements, distributions, q):
    """
    This function implements the proposed algorithm to achieve
    fairness in the IID distributions case.

    args:
        elements (SecInstanceArray): array containing instances
        distributions (list): list containing the order distributions
        q (list): offline fair optimal algorithm selection probabilities 

    returns:
        best candidate object   
    """
    p = (2 / 3) / len(elements)      
    condition = 1 - p / (1 - p * np.arange(len(elements)))
    return filterElements(elements, distributions, condition)