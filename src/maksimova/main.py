import numpy as np
import csv
import matplotlib.pyplot as plt

X = []
Y = []

with open('signal5.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')

    for ROWS in plotting:
        X.append(float(ROWS[0]))
        Y.append(float(ROWS[1]))


def f_coefficients(n):
    my_array = np.zeros((n,))
    k = 0
    while k < n:
        my_array[k] = 1.0 / n
        k += 1
    return my_array


def do_filter(data, coefficients):
    filtered_data = data.copy()
    n = len(coefficients)
    for i in range(n, len(data)):
        # умножаем значения на коэффициенты и суммируем
        filtered_value = sum([data[i - j] * coefficients[j] for j in range(n)])
        # записываем отфильтрованное значение в массив
        filtered_data[i] = filtered_value
    return filtered_data


Y1 = do_filter(Y, f_coefficients(301))
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графики')

ax.plot(X, Y, label='График 1')
ax.plot(X, Y1, label='График 2', linestyle='--', color='red')
ax.legend()
plt.show()
