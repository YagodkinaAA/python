import numpy as np
import matplotlib.pyplot as plt

# part1
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
# y = np.random.normal(0, 2, 500)
# ax.hist(y, 50)  # разбиение на 50 столбцов
x = [f'H{i + 1}' for i in range(10)]
y = np.random.randint(1, 5, len(x))
ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)
ax.grid()

# part2
fig1 = plt.figure(figsize=(6, 4))
ax1 = fig1.add_subplot()
y1 = np.random.normal(0, 2, 500)
x1 = np.linspace(np.min(y1), np.max(y1), 10)  # разбили на 10 равных интервалов
bars = [len(y1[np.bitwise_and(y1 >= x1[i], y1 < x1[i + 1])]) for i in range(len(x1) - 1)]
x2 = [f'H{i + 1}' for i in range(10)]
ax1.bar(range(len(x2) - 1), bars)
# ax1.barh(range(len(x2)-1.2), bars) #чтоб столбцы были относительно 0у
ax1.grid()

# part3
fig3 = plt.figure(figsize=(6, 4))
ax3 = fig3.add_subplot()
x3 = np.arange(10)
a1 = np.random.randint(3, 20, len(x3))
a2 = np.random.randint(3, 20, len(x3))
w = 0.3  # толщина линии
ax3.bar(x3 - w / 2, a1, width=w)
ax3.bar(x3 + w / 2, a2, width=w)
ax3.grid()
plt.show()
