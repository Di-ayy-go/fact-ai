from utils import SecretaryInstance
import pandas as pd
from collections import Counter
import gzip
import pickle

def GetSecretaryInputBank(num_elements):
    df = pd.read_csv('data/bank-additional-full.csv', delimiter=';')
    df = df.head(num_elements)

    instance = []

    for index, row in df.iterrows():
        age = row['age']
        color = int((age - 21) / 10)

        if age <= 30:
            color = 0

        if age > 60:
            color = 4

        instance.append(SecretaryInstance(row['duration'] + index * 0.0000001, color))
    
    color_dis = Counter([element.color for element in instance])
    colors = sorted(color_dis.keys())

    sizes = [color_dis[color] for color in colors]
    num_colors = len(colors)

    # print(num_colors, sizes)
    print(len())

    return instance

def CalculateBMI(weight, height):
    BMI = weight / ((height/100.0)**2)

    if BMI < 18.5:
        return 0

    if 18.5 <= BMI < 25:
        return 1

    if 25.0 <= BMI < 30.0:
        return 2

    if 30.0 <= BMI < 35:
        return 3

    if BMI >= 35.0:
        return 4 
        
    print("ERROR", weight, height)

def GetPokecNodes():
    input_bmi = "data/soc-pokec-profiles.txt.gz"

    nodes = []
    ids = []

    # Calculate BMI and get id
    with gzip.open(input_bmi, 'rt') as in_bmi:
        for line in in_bmi:
            split_line = line.split('	')
            body = split_line[8].split(',')
            
            try:
                height = int(body[0].replace('cm','').strip())
                weight = int(body[1].replace('kg','').strip())
                user_id = int(split_line[0])

                # Only add realistic values
                if (20 <= weight <= 350) and (100 <= height <= 250):
                    nodes.append(CalculateBMI(weight, height))
                    ids.append(user_id)

                # else:
                #     print("Error", weight, height, user_id)

            except:
                pass

    print("Nodes and ids constructed.")

    return nodes, ids

def GetPokecDegrees():
    input_edges = "data/soc-pokec-relationships.txt.gz"

    #column_1 = []
    column_2 = []

    with gzip.open(input_edges, 'rt') as in_edges:
        for line in in_edges:
            split_line = line.replace('\n','').split('	')
            
        
            try:
                # column_2.append(int(split_line[0]))
                column_2.append(int(split_line[1]))

            except:
                print(int(split_line[1]))
                pass

    print("Degrees constructed.")

    return Counter(column_2)

def GetSecretaryInputPokec(num_elements):
    nodes, ids = GetPokecNodes()
    degrees = GetPokecDegrees()
    instance = []

    for i, user_id in enumerate(ids[:num_elements]):
        instance.append(SecretaryInstance(degrees[user_id] + i * 0.0000001, nodes[i]))

    color_dis = Counter([element.color for element in instance])
    colors = sorted(color_dis.keys())

    sizes = [color_dis[color] for color in colors]
    num_colors = len(colors)

    print(num_colors, sizes)

    # with open("data/pokec_instance.dat", "wb") as f:
    #     pickle.dump(instance, f)

    return instance

def GetSecretaryInputUfrgs(num_elements):
    df = pd.read_csv('data/data-UFRGS.csv', header=None)
    instance = []

    for index, row in df.iterrows():
        gender = int(row[0])
        gpa = float(row[10])

        instance.append(SecretaryInstance(gpa + index * 0.0000001, gender))
    
    color_dis = Counter([element.color for element in instance])
    colors = sorted(color_dis.keys())

    sizes = [color_dis[color] for color in colors]
    num_colors = len(colors)

    # print(num_colors, sizes)
    # print(len(instance))

    return instance