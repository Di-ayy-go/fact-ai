import numpy as np

def Eval(instance, answer, num_colors):
    max_value = np.zeros(num_colors)
    correct_answer = np.zeros(num_colors)
    num_answer =  np.zeros(num_colors)

    total_max = 0
    not_picked = 0
    total_correct_answer = 0

    for i in range(len(instance)):
        max_value[instance[i].color] = max([max_value[instance[i].color], instance[i].value])
   
    for i in range(num_colors):
        total_max = max([max_value[i], total_max])

    print('Color Distribution: \n')

    color = np.zeros(num_colors)

    for i in range(len(instance)):
        color[instance[i].color] += 1

    for i in range(num_colors):
        print(color[i])

    print('\n')

    for element in answer:
        # print(element)
        if element.color == -1:
            not_picked += 1
            continue

        num_answer[element.color] += 1
        if (max_value[element.color] - element.value) < 0.0000001:
            correct_answer[element.color] += 1

        if (total_max - element.value) < 0.0000001:
            total_correct_answer += 1

    print('Answer Distribution: \n')

    for i in range(num_colors):
        print(num_answer[i])

    print('\n')
    print('Correct Answer Distribution: \n')

    for i in range(num_colors):
        print(correct_answer[i])

    print('\n')
    print(f"Total Correct Answer: {total_correct_answer}")
    print('Probability Correct Answer: ')
    print(total_correct_answer / len(answer))
    print(f"Total Not Picked: {not_picked}")

    return num_colors, num_answer, correct_answer

def ThEval(instance, answers, num_colors):
    total_max = 0
    not_picked = 0

    total_correct_answer = np.zeros(len(answers))

    for i in range(len(instance)):
        total_max = max([total_max, instance[i].value])

    for i in range(len(answers)):
        for element in answers[i]:
            if element.color == -1:
                not_picked += 1
            if (total_max - element.value) < 0.0000001:
                total_correct_answer[i] += 1
        print(total_correct_answer[i] / len(answers[i]))

    return

def InnerUnbalanced(instance, ans, correct_answer, num_answer, max_dist,
                    num_colors, not_picked, total_correct_answer):

    max_value = np.zeros(num_colors)
    total_max = 0

    max_color = 0

    for element in instance:
        max_value[element.color] = max([max_value[element.color], element.value])
        old_max = total_max
        total_max = max([total_max, element.value])
        if old_max < total_max:
            max_color = element.color

    max_dist[max_color] += 1
    if ans.color == -1:
        not_picked += 1
        return

    num_answer[ans.color] += 1

    if (max_value[ans.color] - ans.value) < 10:
        correct_answer[ans.color] += 1

    if (total_max - ans.value) < 10:
        total_correct_answer += 1

    return
