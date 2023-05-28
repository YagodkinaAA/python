import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure(figsize=(7, 4))  # создали доп. окошко
plt.plot(np.arange(0, 10, 0.2))

fig2 = plt.figure(figsize=(7, 4))
#ax1 = fig2.add_axes([0, 0, 1, 1])
ax1 = fig2.add_subplot(1, 3, 1)
ax1.plot(np.arange(0, 5, 0.2))

f, ax = plt.subplots(2, 2)

# изменим параметры фигуры(figure)
f.set_size_inches(7, 4)  # размер 7 х 4 дюймов
f.set_facecolor('#7FFFD4')  # цвет фона

ax[0, 0].plot(np.arange(0, 5, 0.2))
ax[0, 0].grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
ax[0, 1].grid()
plt.show()
