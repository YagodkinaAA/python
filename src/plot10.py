import numpy as np
import matplotlib.pyplot as plt

#part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)
ax.step(x, x, '-go')
ax.grid()


#part2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()

x1 = np.arange(0, 10)
ax1.step(x1, x1, '-ro', where='post')
ax1.grid()

#part2
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
x2 = np.arange(0, 10)
ax2.step(x2, x2, '-yo', where='mid')
ax2.grid()

#part3
fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()
x3 = np.arange(0, 10)
ax3.step(x3, x3, '-yo', x3, np.cos(x3), '--x', where='mid')
ax3.grid()

#part4
fig4 = plt.figure(figsize=(4, 4))
ax4 = fig4.add_subplot()
x4 = np.arange(-2, 2, 0.1)
y1 = np.array([-y**2 for y in x4]) + 8
y2 = np.array([-y**2 for y in x4]) + 8
y3 = np.array([-y**2 for y in x4]) + 8
ax4.set(xlim=(-2, 2), ylim=(0, 25))
ax4.stackplot(x4, y1, y2, y3)
ax4.grid()

#part5
fig5 = plt.figure(figsize=(7, 4))
ax5 = fig5.add_subplot()
x5 = np.arange(-np.pi, np.pi, 0.3)
ax5.stem(x5, np.cos(x5), '--', bottom=0.5)
ax5.grid()

#part6
fig6 = plt.figure(figsize=(7, 4))
ax6 = fig6.add_subplot()
x6 = np.random.normal(0, 2, 500)
y6 = np.random.normal(0, 2, 500)
ax6.scatter(x6, y6, s=50, c='g', linewidths=1, marker='s', edgecolors='r')
ax6.grid()
plt.show()