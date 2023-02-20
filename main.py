import numpy as np
from numpy import ndarray

# 1 задание

print('1.')
line: ndarray = np.arange(1, 10)
multiplication_table: ndarray = line * line[:, None]
print(multiplication_table)
print()

# 2 задание
print('2.')

def ar_progress(N: int, elem_1: float, d: float):
    mas = np.eye(N)
    for i in range(0, N):
        mas[i][i] = elem_1
        elem_1 += d
    return mas


print(ar_progress(6, 1, 0.2))
print()

#3 задание
print('3.')

A = np.arange(1, 26).reshape(5, 5)
print(A)
print()

#4 задание
print('4.')

print(np.pad(np.zeros(4).reshape(2,2), (1, 1), 'constant', constant_values = 1))
print()


#5 задание
print('5.')

