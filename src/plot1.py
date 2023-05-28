import numpy as np
import matplotlib.pyplot as plt

# fig1
ax1 = plt.subplot(1, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(1, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(1, 3, 3)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()

# fig2
a1 = plt.subplot(2, 3, 1)
plt.plot(np.random.random(10))
a2 = plt.subplot(2, 3, 2)
plt.plot(np.random.random(10))
a3 = plt.subplot(2, 3, 3)
plt.plot(np.random.random(10))
a4 = plt.subplot(2, 1, 2)
plt.plot(np.random.random(10))
a1.grid()
a2.grid()
a3.grid()
a4.grid()
plt.show()
