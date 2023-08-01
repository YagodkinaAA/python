import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

# part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.2))
# ax.set(xlim=(-5, 30), ylim=(-1.2, 6))
'''ax.set_xlim(xmin=-5, xmax=10)
ax.set_ylim(-1.2, 6)'''
# если график только один, то можно использовать функцию plt, но значения применятся только к той оси, что написана выше
plt.xlim(-1, 20)
plt.ylim(-1, 6)

# part2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()
ax1.plot(np.random.random(10))
lc = NullLocator()
ax1.grid()
ax1.xaxis.set_major_locator(lc)
# ax1.xaxis.set_major_locator(NullLocator())

# part3
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
ax2.plot(np.random.random(10))
ax2.grid()
ax2.yaxis.set_major_locator(LinearLocator(5))

# part4
fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()
ax3.plot(np.arange(1, 5, 0.2))
ax3.grid()
ax3.xaxis.set_major_locator(MultipleLocator(base=3.5))

# part5
fig4 = plt.figure(figsize=(7, 4))
ax4 = fig4.add_subplot()
i = np.arange(-np.pi / 2, np.pi, 0.1)
ax4.plot(i, np.sin(i))
ax4.grid()
ax4.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))

# part6
fig5 = plt.figure(figsize=(7, 4))
ax5 = fig5.add_subplot()
s = np.arange(-np.pi / 2, np.pi, 0.1)
ax5.plot(s, np.sin(s))
ax5.grid()
ax5.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))

#part7
fig6 = plt.figure(figsize=(7, 4))
ax6 = fig6.add_subplot()
z = np.arange(-np.pi / 2, np.pi, 0.1)
ax6.plot(z, np.sin(z))
ax6.grid()
ax6.xaxis.set_major_locator(LogLocator(base=2))

#part8
fig7 = plt.figure(figsize=(7, 4))
ax7 = fig7.add_subplot()
a = np.arange(1, 10, 0.1)
ax7.plot(a, np.log(a))
ax6.grid()
ax6.xaxis.set_major_locator(MaxNLocator(7))


#part9
fig8 = plt.figure(figsize=(7, 4))
ax8 = fig8.add_subplot()
r = np.arange(-np.pi / 2, np.pi, 0.1)
ax8.plot(r, np.sin(r))
#включаем минорную сетку
ax8.minorticks_on()
ax8.grid(which='major', lw=2)
ax8.grid(which='minor')
ax8.xaxis.set_minor_locator(NullLocator())
plt.show()

