import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update_cos(frame, line, x):
    # frame-параметр, который меняется от кадра к кадру, в нашем случае это начальная фаза(угол)
    # line-ссылка на объект Line2D
    line.set_ydata(np.cos(x + frame))
    return [line]


# plt.ion() при использовании объекта класса этот режим включается и выключается автоматически
fig, ax = plt.subplots()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)
line, = ax.plot(x, y)

phasa = np.arange(0, 4 * np.pi, 0.1)

# создаем экземпляр класса
animation = FuncAnimation(
    fig,  # фигура, где отображается анимация
    func=update_cos,  # функция обновления текущего кадра
    frames=phasa,  # параметр, меняющийся от кадра к кадру
    fargs=(line, x),  # дополнительные параметры для функции update_cos
    interval=30,  # задержка между кадрами в мс
    blit=True,  # использовать ли данную буферизацию
    repeat=False)  # зацикливать ли анимацию

# plt.ioff()
plt.show()
