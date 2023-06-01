import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

l1 = Line2D([1, 2, 3], [1, 2, 4]) #ломаная в [] координаты

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos = Line2D(x, np.cos(x))

rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')
#part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25), '--o', label='line 1')
ax.plot(np.arange(0, 10, 0.5), ':s',  label='line 2')
#ax.legend(loc='upper right')
#ax.legend([1, 2], bbox_to_anchor=(0.5, 0.7))
line1, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line 1')
line2, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line 2')
#ax.legend((line2, line1), ['Линия 2', 'Линия 1'])
#ax.legend((line2, line1), [r'$f(x) = a \cdot b + c$', r'$f(x) = k \cdot x +b$'], facecolor='#aaa', framealpha=0.5)
ax.add_line(cos)

#part2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()
ax1.add_line(l1)
ax1.add_patch(rect)
ax1.set(xlim=(-1, 3), ylim=(-1, 4)) #задали пределы у осей
plt.show()
