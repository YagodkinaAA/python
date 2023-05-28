import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

#размер столбцов и строк(какую долю от общего размера будет занимать столбец и строка)
ws = [1, 2, 5]
hs = [2, 0.5]

fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)

ax1 = plt.subplot(gs[0, 0])
plt.plot(np.arange(0, 5, 0.2))
ax2 = fig.add_subplot(gs[1, 0:2])
plt.plot(np.random.random(10))
ax3 = fig.add_subplot(gs[:, 2])
plt.plot(np.random.random(10))
plt.show()
