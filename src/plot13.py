import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#part1(двумерный график в трех измерениях)
fig = plt.figure(figsize=(7, 4))
#ax_3d = Axes3D(fig)  # создали трехмерную ось
ax_3d = fig.add_subplot(projection='3d')
x = np.linspace(0, 10, 50)
z = np.cos(x)
ax_3d.plot(x, x, z)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

#part2(каркасная сетка)
fig1 = plt.figure(figsize=(7, 4))
ax1_3d = fig1.add_subplot(projection='3d')
'''a = [1.2, 2, 3] #определяет положение столбцов
b = [2, 5, 6, 8] #определяет положение строк
agrid, bgrid = np.meshgrid(a, b) #сформировали двумерный массив
print(f'agrid={agrid}, bgrid= {bgrid}')
print(f'({agrid[1.2, 2]}, {bgrid[1.2, 2]})')'''
x1 = np.arange(-2*np.pi, 2*np.pi, 0.2)
y1 = np.arange(-2*np.pi, 2*np.pi, 0.2)
x1grid, y1grid = np. meshgrid(x1, y1)
z1grid = np.sin(x1grid) * np.sin(y1grid) / (x1grid * y1grid)
ax1_3d.plot_wireframe(x1grid, y1grid, z1grid)

#part3(непрерывная поверхность)
fig2 = plt.figure(figsize=(7, 4))
ax2_3d = fig2.add_subplot(projection='3d')
x2 = np.arange(-2*np.pi, 2*np.pi, 0.2)
y2 = np.arange(-2*np.pi, 2*np.pi, 0.2)
x2grid, y2grid = np. meshgrid(x2, y2)
z2grid = np.sin(x2grid) * np.sin(y2grid) / (x2grid * y2grid)
ax2_3d.plot_surface(x2grid, y2grid, z2grid, rstride=2, cstride=2, cmap='plasma')

#part4(точечный график)
fig3 = plt.figure(figsize=(7, 4))
ax3_3d = fig3.add_subplot(projection='3d')
x3 = np.arange(-2*np.pi, 2*np.pi, 0.2)
y3 = np.arange(-2*np.pi, 2*np.pi, 0.2)
x3grid, y3grid = np. meshgrid(x3, y3)
z3grid = np.sin(x3grid) * np.sin(y3grid) / (x3grid * y3grid)
ax3_3d.scatter(x3grid, y3grid, z3grid, s=1, color='g')
plt.show()
