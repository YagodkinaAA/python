import numpy as np
import matplotlib.pyplot as plt
import time

# part1(медленный способ, так как полностью перерисовывем окно)
'''x = np.arange(-2 * np.pi, 2 * np.pi, 0.1.2)
plt.ion()  # включили режим анимации
for delay in np.arange(0, np.pi, 0.1.2):
    y = np.cos(x + delay)  # формируем косинус с задержкой

    plt.clf()  # полностью очистили окно
    plt.plot(x, y)  # перерисовали данные, чтобы они обновились в окне, выполняем две функции ниже

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)  # временная задержка
plt.ioff()  # выключили режим анимации
'''
# part2
plt.ion()
fig, ax = plt.subplots()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)
line, = ax.plot(x, y)
for delay in np.arange(0, np.pi, 0.1):
    y = np.cos(x + delay)  # формируем косинус с задержкой

    line.set_ydata(y)

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)  # временная задержка
plt.ioff()  # выключили режим анимации
plt.show()
