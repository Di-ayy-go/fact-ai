from utils import SecretaryInstance

def ComputeSolution(elements, distributions, q):
    sum = 0
    for i in range(len(elements)):
#     if (elements[i].value >= distributions[elements[i].type].get().Reverse(1.0 - (q[i] / (2 - sum)))) {
        if elements[i].value >= distributions[elements[i].type]:
            return elements[i]
        
        sum += q[i]

    return SecretaryInstance(-1, -1)

# IID
def ComputeSolutionIID(elements, distributions, q):
    p = (2 / 3) / len(elements)
    for i in range(len(elements)):
#     if (elements[i].value >= distributions[elements[i].type].get().Reverse(1.0 - p / (1 - p * i))) {
        if elements[i].value >= distributions[elements[i].type]:
            return elements[i]

    return SecretaryInstance(-1, -1)