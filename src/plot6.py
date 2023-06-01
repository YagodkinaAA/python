import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter


# matplotlib.rcParams['axes.formatter.limits'] = (-4, 4) если хотим применить лимит степени для всех графиков 


def format0y(x, pos):
    return f'[{x}]' if x < 0 else f'({x})'


# part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax.plot(x, np.sin(x))
'''ax.set_xticklabels([])
ax.set_yticklabels([])'''
ax.yaxis.set_major_formatter(NullFormatter())
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))  # целые числа
ax.grid()

# part2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax1.plot(x, np.sin(x))
ax1.xaxis.set_major_formatter(FormatStrFormatter('%d'))  # дробные числа
ax1.yaxis.set_major_formatter(FormatStrFormatter('y= %.1f'))
ax1.grid()

# part3
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax2.plot(x, np.sin(x))
ax2.yaxis.set_major_formatter(FuncFormatter(format0y))
ax2.grid()

# part4
fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax3.plot(x, np.sin(x) * 1e5)
sf = ScalarFormatter()
sf.set_powerlimits((-4, 4))  # если степень выходит из этого предела, то она выносится
ax3.yaxis.set_major_formatter(sf)
ax3.grid()

# part4
fig4 = plt.figure(figsize=(7, 4))
ax4 = fig4.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax4.plot(x, np.sin(x) * 1e5)
ax4.xaxis.set_major_formatter(FixedFormatter([-3, -2, -1, 0, 1, 2, 3]))
ax4.yaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'f', 'e']))
ax4.grid()
plt.show()
