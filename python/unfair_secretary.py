from utils import SecretaryInstance
from random_handler import RandomHandler
import numpy as np
import sys

rh = RandomHandler()
def ComputeSolution(elements):
    """
    This function returns the best candidate for a list
    of candidates, using the SA algorithm.

    args:
        elements (list): list of candidates

    returns:
        best candidate object
    """

    max_value = 0

    th = int(len(elements) * (1.0 / np.exp(1.0)))

    # compute max values
    for i in range(0, th):
        max_value = max(max_value, elements[i].value)

    for i in range(th, len(elements)):
        if elements[i].value >= max_value:
            return elements[i]

    return SecretaryInstance(-1, -1)


def ComputeSolutionOpt(elements, element_values):
    max_value = 0

    th = int(len(elements) * (1.0 / np.exp(1.0)))
    max_value = np.max(element_values[:th])
            
    sliced_val = np.array(element_values[th:])
    indice_matches = np.where(sliced_val >= max_value)

    if len(indice_matches[0]) == 0:
        return SecretaryInstance(-1, -1)

    else:
        return elements[(np.min(indice_matches) + th)]


def ComputeSolutionSingleColor(elements, prob):
    """
    This function returns the best candidate for a list
    of candidates, using the SCSA algorithm.

    args:
        elements (list): list of candidates
        prob (list): list of probabilties used by algorithm

    returns:
        best candidate object
    """

    max_value = 0
    rand_color = 0

    rand = rh.eng() % 1e6
    rand_balanced = rand / 1e6

    for i in range(len(prob)):
        if rand_balanced <= prob[i]:
            rand_color = i
            break
        rand_balanced -= prob[i]

    th = int(len(elements) * (1.0 / np.exp(1.0)))

    # compute max values
    for i in range(0, th):
        if rand_color == elements[i].color:
            max_value = max(max_value, elements[i].value)

    for i in range(th, len(elements)):
        if elements[i].value >= max_value and elements[i].color == rand_color:
            return elements[i]

    return SecretaryInstance(-1, -1)


def ComputeSolutionSingleColorOpt(elements, element_colors, element_values, prob):
    """
    This function returns the best candidate for a list
    of candidates, using the SCSA algorithm.

    args:
        elements (list): list of candidates
        element_colors (np.array): list of colors/groups of each candidate
        element_values (np.array): list of values of each candidate
        prob (list): list of probabilties used by algorithm

    returns:
        best candidate object
    """

    max_value = 0
    rand_color = 0

    rand = rh.eng() % 1e6
    rand_balanced = rand / 1e6

    for i in range(len(prob)):
        if rand_balanced <= prob[i]:
            rand_color = i
            break
        rand_balanced -= prob[i]

    th = int(len(elements) * (1.0 / np.exp(1.0)))

    color_indices = np.where(np.array(element_colors[:int(th)])==rand_color)

    if len(color_indices[0]) != 0:
        max_value = np.max(element_values[color_indices])
            
    else:
        max_value = sys.maxsize

    sliced_col = np.array(element_colors[th:])
    sliced_val = np.array(element_values[th:])
    indice_matches = np.intersect1d(np.where(sliced_col==rand_color), np.where(sliced_val >= max_value))

    if len(indice_matches) == 0:
        return SecretaryInstance(-1, -1)
    
    else:
        return elements[np.min(indice_matches) + th]