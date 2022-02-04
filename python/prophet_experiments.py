import utils
import fair_prophet as fp
import unfair_prophet as ufp 
import synthetic_data as syn_data
from utils import SecretaryInstance, GetThreshold, ComputeThreshold
import secretary_eval as se

import numpy as np
from collections import defaultdict
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd


def ProphetExperiment(size, num_rep, distributions):
    """
    This function runs the experiment for all prophet algorithms. 

    args:
        size (int): number of colors/groups
        num_rep (int): number of experiment repetitions
        distributions (list): list containing arrival order distributions

    returns:
        data (dict): results of experiments to plot
    """
    q = np.ones(size) / size
    
    answers = defaultdict(list)
    for _ in tqdm(range(num_rep)):
        instance = syn_data.GetProphetInput(size, distributions)
        answers['Fair PA'].append(fp.ComputeSolution(instance, distributions, q))
        answers['Fair IDD'].append(fp.ComputeSolutionIID(instance, distributions, q))
        answers['SC'].append(ufp.ComputeSolutionOneHalf(instance, distributions, q))
        answers['EHKS'].append(ufp.ComputeSolutionMinusOneE(instance, distributions, q))
        answers['DP'].append(ufp.ComputeSolutionThreeForth(instance, distributions, q))
        answers['CFHOV'].append(ufp.ComputeSolutionDiffEq(instance, distributions, q))
    return instance, answers


def PlotProphet(num_rep, size, distributions, file_name, printeval):
    """
    This function creates a plot of all experiment results. 

    args:
        num_rep (int): description of var

    args:
        num_rep (int): number of experiment repetitions
        size (int): number of colors/groups
        distributions (list): list containing arrival order distributions
        file_name (string): output plot location

    returns:
        data (dict): description of return val
    """
    data = {}

    # Generate data for plot
    instance, results = ProphetExperiment(size, num_rep, distributions)

    # Add results to data    
    for name, result in results.items():
        
        # Remove results where no candidate was picked
        result = list(filter(lambda val: val.color !=  -1, result))
        result_col = [i.color for i in result]
        result_val = np.sum([i.value for i in result]) / num_rep
        data[name] = np.histogram(result_col, np.arange(size + 1))[0]

        print(f"\n{name}\nAverage value of chosen candidate: {result_val}")
        if printeval:
            se.Eval(instance, result, size)
    
    # Create plot
    plt.figure(figsize=(15, 8))
    df = pd.DataFrame.from_dict(data, orient='columns')
    
    # As in the paper, this result distorts the plot so it is omitted from the visualization.
    try:
        df = df.drop("DP", axis=1)
    except:
        pass

    ax = df.plot.line()
    ax.set_ylabel('Num Picked')
    ax.set_xlabel('Arrival Position')
    plt.savefig(file_name, bbox_inches='tight', dpi=400)
    plt.show()

    return data