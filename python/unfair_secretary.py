from utils import SecretaryInstance
from random_handler import RandomHandler
import numpy as np

rh = RandomHandler()
def ComputeSolution(elements):
    max_value = 0

    th = int(len(elements) * (1.0 / np.exp(1.0)))

    # compute max values
    for i in range(0, th):
        max_value = max(max_value, elements[i].value)

    for i in range(th, len(elements)):
        if elements[i].value >= max_value:
            return elements[i]

    return SecretaryInstance(-1, -1)
    

def ComputeSolutionSingleColor(elements, prob):
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