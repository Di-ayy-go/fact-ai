from utils import SecretaryInstance
import numpy as np
import sys

def ComputeSolution(elements, num_colors, thre):
    """
    This function returns the best candidate for a list
    of candidates, using the secretary algorithm.

    args:
        elements (list): list of candidates
        num_colors (int): number of colors of candidates
        thre (list): list of thresholds used by algorithm

    returns:
        best candidate object
    """

    max_color = num_colors * [0]
    # Compute max values
    for i in range(len(elements)):
        if i < thre[elements[i].color]:
            max_color[elements[i].color] = max([max_color[elements[i].color], elements[i].value])

    # Return best candidate
    for i in range(len(elements)):
        if i >= thre[elements[i].color]:
            if elements[i].value >= max_color[elements[i].color]:
                return elements[i]

    return SecretaryInstance(-1, -1)

def ComputeSolutionOpt(elements, element_colors, element_values, num_colors, thre):
    max_color = np.zeros(num_colors)

    for i in range(len(max_color)):
        threshold = thre[i]
        color_indices = np.where(np.array(element_colors[:int(threshold)])==i)

        if len(color_indices[0]) != 0:
            max_color[i] = np.max(element_values[color_indices])
            
        else:
            max_color[i] = sys.maxsize

    all_indices = np.array([], dtype=int)

    for i in range(len(max_color)):
        threshold = int(thre[i])
        sliced_col = np.array(element_colors[threshold:])
        sliced_val = np.array(element_values[threshold:])
        indice_matches = np.intersect1d(np.where(sliced_col==i), np.where(sliced_val >= max_color[i]))
        all_indices = np.append(all_indices, (indice_matches + threshold))

    if len(all_indices) == 0:
        return SecretaryInstance(-1, -1)
    
    else:
        return elements[np.min(all_indices)]