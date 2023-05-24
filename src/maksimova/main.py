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


def f_coefficients(n, k=0):
    my_array = np.zeros((n,))
    while k < n:
        my_array[k] = (-12 * k + 6 * (n - 1)) / (n ** 3 - n)
        k += 1
    return my_array


def f_coefficients1(n):
    window = np.ones(int(n)) / float(n)
    return window


def do_filter(data, n, coefficients):
    filtered_data = data.copy()
    for i in range(n, len(data)):
        # умножаем значения на коэффициенты и суммируем
        filtered_value = sum([data[i - j] * coefficients[j] for j in range(n)])
        # записываем отфильтрованное значение в массив
        filtered_data[i] = filtered_value
    return filtered_data


n = 301
k = f_coefficients1(n)
Y1 = do_filter(Y, n, k)
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графики')

# добавляем два графика
ax.plot(X, Y, label='График 1')
ax.plot(X, Y1, label='График 2', linestyle='--', color='red')

# добавляем легенду
ax.legend()

# отображаем графики
plt.show()
