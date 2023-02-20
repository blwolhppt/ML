import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

dataset = pd.read_csv('Вариант 2.csv', delimiter=',',
                      names=['№ школы', 'Класс', 'Пол', 'Номер варианта',
                             'Задания с кратким ответом',
                             'Задания с развёрнутым ответом',
                             'Первичный балл', 'Балл', 'Минимальный балл'])

# print(dataset)
#
# avg: float = 49.26
print(f'Процент людей, у которых результат меньше среднего значения: '
      f'{"%.2f" % (len(dataset.query("Балл < 49.26")) * 100 / len(dataset))}%')

print()
print(f'Процент людей, которые не сдали экзамен: '
      f'{"%.2f" % (len(dataset.query("Балл < 27")) * 100 / len(dataset))} %')

plt.pie(
    x=[len(dataset.query("Балл > 27")), len(dataset.query("Балл < 27"))],
    labels=['Сдали экзамен', 'Не сдали экзамен'])
plt.show()

s = pd.Series(dataset['Балл'])
ax = s.plot.kde()
ax.set_title('Ядерная оценка плотности распределения баллов')
plt.show()

print()
print(f'Процентное соотношение оценок учащихся: '
      f'{"%.2f" % (len(dataset.query("67 < Балл")) * 100 / len(dataset))} % - 5, '
      f'{"%.2f" % (len(dataset.query("49<Балл<68")) * 100 / len(dataset))} % - 4, '
      f'{"%.2f" % (len(dataset.query("26<Балл<50")) * 100 / len(dataset))} % - 3, '
      f'{"%.2f" % (len(dataset.query("Балл < 27")) * 100 / len(dataset))} % - 2')

print()
print(f'Процентное соотношение девушек и юношей: '
      f'{round((len(dataset[dataset.Пол == "Ж"])) * 100 / len(dataset))} % '
      f'и {round((len(dataset[dataset.Пол == "М"])) * 100 / len(dataset))} %')

print()
print(f'Кол-во школ, принимавших участие в экзамене: '
      f'{len(dataset["№ школы"].value_counts())}')

print()
print(
    f'Заданий с кратким ответом: {len(str(dataset["Задания с кратким ответом"][2:3]).split()[1])} \n'
    f'Заданий с развернутым ответом: {len(str(dataset["Задания с развёрнутым ответом"][2:3]).split()[1]) // 4}')

print()
print(
    'Процент выполненных и невыполненных заданий по каждому вопросу класса В:')
df = pd.DataFrame(np.array(dataset['Задания с кратким ответом']))
for i in range(1, 13):
    num = df[0].str.split('').str[i]
    x = 0
    y = 0
    for elem in num:
        if elem == '-':
            x += 1
        else:
            y += 1

    print(f'·{i} задание: {round(y * 100 / len(dataset))}% - верно, '
          f'{round(x * 100 / len(dataset))}% - неверно')

print()
print(
    'Процент выполненных и невыполненных заданий по каждому вопросу класса C:')
df = pd.DataFrame(np.array(dataset['Задания с развёрнутым ответом']))

number = 0
for i in range(1, 26, 4):
    num = df[0].str.split('').str[i]
    x = 0
    y = 0
    for elem in num:
        if int(elem) > 0:
            x += 1
        else:
            y += 1
    number += 1
    print(f'·{number} задание: {round(x * 100 / len(dataset))}% - верно, '
          f'{round(y * 100 / len(dataset))}% - неверно')


print()
print('Сравнение двух школ')
df = pd.DataFrame(np.array(dataset.loc[dataset['школа'] == 124, 'Задания с кратким ответом']))
number = 0
for i in range(1, 26, 4):
    num = df[0].str.split('').str[i]
    x_124 = 0
    y_124 = 0
    for elem in num:
        if elem == '+':
            x_124 += 1
        else:
            y_124 += 1
    number += 1
    print(f'·{number} задание: {round(x * 100 / len(df))}% - верно, '
          f'{round(y * 100 / len(df))}% - неверно')