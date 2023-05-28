# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# matplotlib.use('Qt5Agg')
# print(matplotlib.get_backend())
# fig1
x = np.array([4, 5, 6, 7, 8])
y = np.array([1, 2, -6, 0, 4])
plt.plot(x, y)
plt.show()
# fig2
q = np.array([1, 1, 5, 5, 1])
w = np.array([1, 5, 5, 1, 1])
lines = plt.plot(x, y, q, w)
plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='b', linewidth=4)
plt.show()
# fig3
f = np.arange(0, 5, 1)
g = np.array([a * a for a in f])
s = [0, 1, 2, 3]
e = [i + 1 for i in s]
plt.plot(g, f, 'o--m', e, s, 'x:k')
plt.grid()
plt.show()
plt.plot(x, y, '*')
plt.plot(q, w, ':')
plt.show()
# fig4
lines1 = plt.plot(e, s, g, f, color='g', marker='v', markerfacecolor='w')
print(lines1)
plt.setp(lines1, linestyle='-.')
plt.show()
# fig5
h = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
j = np.cos(h)
plt.fill_between(h, j)
plt.grid()
plt.show()
plt.fill_between(h, j, where=(j < 0), color='r', alpha=0.5)
plt.fill_between(h, j, where=(j > 0), color='g', alpha=0.5)
plt.grid()
plt.show()
