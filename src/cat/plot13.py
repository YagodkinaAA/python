import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# part1
img = Image.open('cat.jpg')
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
ax.imshow(img)
# plt.imshow(img) можем использовать если у нас одно изображение и одни оси

# part2
img1 = Image.open('cat_griff.png')
fig1 = plt.figure(figsize=(6, 4))
ax1 = fig1.add_subplot()
ax1.imshow(img1)

# part3
fig2 = plt.figure(figsize=(6, 4))
data = np.random.randint(0, 255, (100, 100))
ax2 = fig2.add_subplot()
ax2.imshow(data, cmap='plasma')

# part4
img2 = np.array(Image.open('cat_black.png'))
fig3 = plt.figure(figsize=(6, 4))  # цвет картинки не меняется(
ax3 = fig3.add_subplot()
d = ax3.imshow(img2, origin='lower', cmap='spring', aspect='equal', alpha=1)
plt.colorbar(d)

# part5
fig4 = plt.figure(figsize=(6, 4))
data1 = np.random.randint(0, 255, (10, 10))
ax4 = fig4.add_subplot()
a = ax4.pcolormesh(data1, edgecolor='black', cmap='spring')
plt.colorbar(a)

plt.show()
