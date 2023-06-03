import numpy as np
import matplotlib.pyplot as plt

# part1(трехмерные оси)
fig1 = plt.figure(figsize=(7, 4))
ax1_3d = fig1.add_subplot(projection='3d')
x1 = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y1 = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
x1grid, y1grid = np.meshgrid(x1, y1)
z1grid = np.sin(x1grid) * np.sin(y1grid) / (x1grid * y1grid)
ax1_3d.contour(x1grid, y1grid, z1grid)
fig2 = plt.figure(figsize=(7, 4))
ax2_3d = fig2.add_subplot(projection='3d')
ax2_3d.contourf(x1grid, y1grid, z1grid)

# part2(двумерные оси)
fig3, ax3 = plt.subplots(1, 2)  # создали фигуру с двумя осями координат
x3 = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y3 = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
x3grid, y3grid = np.meshgrid(x3, y3)
z3grid = np.sin(x3grid) * np.sin(y3grid) / (x3grid * y1grid)
#c1 = ax3[0].contour(x3grid, y3grid, z3grid, 15)#15 линий уровня
#c1 = ax3[0].contour(x3grid, y3grid, z3grid, [-0.5, -0.2, 0, 0.2, 0.5], colors=['g', 'b', 'r'])#передали те линиий, которые хотим отобразить
c1 = ax3[0].contour(x3grid, y3grid, z3grid, cmap='plasma')
ax3[1].contourf(x3grid, y3grid, z3grid)
#ax3[0].clabel(c1)
c1.clabel(colors='k', fmt='%.2f')

#part3
fig4, ax4 = plt.subplots()  # создали фигуру с одной осью координат
x = np.random.rand(100) * 4*np.pi - 2*np.pi #создали 100 чисел в диапазоне от -2пи до 2пи
y = np.random.rand(100) * 4*np.pi - 2*np.pi
z = np.sin(x) * np.sin(y) / (1+np.abs(x * y))
c = ax4.tricontour(x, y, z, cmap='spring')
#c = ax4.tricontourf(x, y, z, cmap='spring')
c.clabel(colors='g')
plt.show()
