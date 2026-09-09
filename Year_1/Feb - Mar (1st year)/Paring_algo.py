import random

list_1 = [31, 88, 91, 51, 12, 27, 44, 86, 99, 79]

list_2 = [66, 74, 76, 52, 34, 39, 97, 18, 11, 6]

list_3 = []

random.shuffle(list_1)
random.shuffle(list_2)

for x in list_1:
    pair = [list_1[x], list_2[x]]
    list_3.append(pair)
    print(list_3)
