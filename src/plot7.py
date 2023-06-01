import numpy as np
import matplotlib.pyplot as plt
#part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-10*np.pi, 10*np.pi, 0.5)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.set_yscale('log', base=10, subs=[2, 9]) #переопределили масштаб для оси у на логарифмический, base-основание логарифма(по умолчанию 10)
#ax.semilogy(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.grid()

#part2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()
x = np.arange(-10*np.pi, 10*np.pi, 0.1)
ax1.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax1.set_xscale('symlog', linthresh=2)
ax1.grid()

#part2
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
x = np.arange(-10*np.pi, 10*np.pi, 0.1)
ax2.loglog(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax2.grid()
plt.show()