def FairSecretaryAlgorithm(instance, num_colors, thre):
    max_color = num_colors * [0]

    # Compute max values
    for i in range(len(instance)):
        if i < thre[instance[i].color]:
            max_color[instance[i].color] = max([max_color[instance[i].color], instance[i].value])

    # Return best candidate
    for i in range(len(instance)):
        if i >= thre[instance[i].color]:
            if instance[i].value >= max_color[instance[i].color]:
                return instance[i]

    return instance[-1]