import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

dataset = pd.read_csv('Вариант 2.csv', delimiter=',',
                      names=['школа', 'Класс', 'Пол', 'Номер варианта',
                             'Задания с кратким ответом',
                             'Задания с развёрнутым ответом',
                             'Первичный балл', 'Балл', 'Минимальный балл'])





df = pd.DataFrame(np.array(dataset.loc[dataset['школа'] == 124, 'Задания с кратким ответом']))
print(df)
number = 0
for i in range(1, 26, 4):
    num = df[0].str.split('').str[i]
    x = 0
    y = 0
    for elem in num:
        if elem == '+':
            x += 1
        else:
            y += 1
    number += 1
    print(f'·{number} задание: {round(x * 100 / len(df))}% - верно, '
          f'{round(y * 100 / len(df))}% - неверно')
