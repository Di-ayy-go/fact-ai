import distributions
import fair_secretary as fs
import synthetic_data as syn_data
import numpy as np
import secretary_eval as se

def GetThreshold(p):
    t = len(p) * [0]
    k = len(p)
    t[k - 1] = (1 - (k - 1) * p[k - 1]) ** (1 / (k - 1))
    for i in range(k - 2, 0, -1):
        sum = 0

        for r in range(i + 1):
            sum += p[r]

        sum /= i

        t[i] = t[i + 1] * ((sum - p[i]) / (sum - p[i + 1])) ** (1 / i)

    t[0] = t[1] * np.exp(p[1] / p[0] - 1)
    return t

def ComputeThreshold(max_size):
    t = (max_size + 1) * [0]
    for i in range(1, max_size):
        p = (i + 1) * [1.0 / (i + 1)]
        t[i + 1] = GetThreshold(p)[0]

    return t

def SecretaryExperiment(sizes, prob, num_rep):
    num_colors = len(sizes)
    answer = []
    instance = syn_data.GetSecretaryInput(sizes, prob)
    threshold = ([i * ComputeThreshold(20)[num_colors] for i in sizes])

    for _ in range(num_rep):
        np.random.shuffle(instance)
        answer.append(fs.FairSecretaryAlgorithm(instance, 4, threshold))

    se.Eval(instance, answer, num_colors)


num_rep = 100
num_colors = 4

# Synthetic dataset, general p values
sizes = [10, 100, 1000, 10000]
prob = [0.3, 0.25, 0.25, 0.2]
SecretaryExperiment(sizes, prob, num_rep)

# Synthetic dataset, general p values
sizes = [10, 100, 1000, 10000]
prob = [0.25, 0.25, 0.25, 0.25]
SecretaryExperiment(sizes, prob, num_rep)
