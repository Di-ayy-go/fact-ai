import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def PlotInstanceDistribution(instance, name):
    x_lim = {
        'Bank' : 2000,
        'Pokec' : 350,
        'Urfgs' : 4 
    }

    labels = {
        'Bank' : ['Before 30', '31-40', '41-50', '51-60', 'After 60'],
        'Pokec' : ['Under', 'Normal', 'Over', 'Obese 1', 'Obese 2'],
        'Urfgs' : ['Female', 'Male']
    }

    plot_colors = {
        'Bank' : ['cornflowerblue', 'salmon', 'wheat', 'dimgrey', 'rebeccapurple'],
        'Pokec' : ['cornflowerblue', 'salmon', 'wheat', 'dimgrey', 'rebeccapurple'],
        'Urfgs' : ['cornflowerblue', 'salmon']
    
    }
    color_dis = Counter([element.color for element in instance])
    colors = sorted(color_dis.keys())
    num_colors = len(colors)
  

    in_colours = []
    in_values = []

    for element in instance:
        in_colours.append(element.color)
        in_values.append(element.value)
    
    in_colours = np.array(in_colours)
    in_values = np.array(in_values)

    data = [in_values[np.where(in_colours == color)] for color in colors]

    plt.figure()
    plt.hist(data, 20, histtype='bar', density=True, label = labels[name], color=plot_colors[name])
    plt.title("Distribution of the {} data set".format(name))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.xlim([0, x_lim[name]])
    plt.savefig("distributions/dataset_distribution_{}.png".format(name), dpi=400)
    plt.show