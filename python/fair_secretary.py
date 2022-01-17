from utils import SecretaryInstance

def FairSecretaryAlgorithm(elements, num_colors, thre):
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
