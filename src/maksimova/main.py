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

    for k in range(n):
        my_array[k] = (-12.0 * k + 6.0 * (n - 1)) / (n ** 3 - n)
    return my_array


def do_filter(data, coefficients):
    filtered_data = data.copy()
    n = len(coefficients)
    for i in range(n, len(data)):
        filtered_data[i] = sum([data[i - j] * coefficients[j] for j in range(n)]) * 1000
    return filtered_data

n = 301
Y1 = do_filter(Y, f_coefficients(n))

for i in range(n):
    Y1[i] = 0

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графики')

ax.plot(X, Y, label='График 1.2')
ax.plot(X, Y1, label='График 2', linestyle='--', color='red')
ax.legend()
plt.show()
