import numpy as np
import matplotlib.pyplot as plt

#part1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp = (0.1, 0.2, 0, 0, 0)
ax.pie(vals, labels=labels, autopct='%.2f', explode=exp, shadow=True)
ax.grid()

#part1
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()
vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp = (0.1, 0.2, 0, 0, 0)
ax1.pie(vals, labels=labels, autopct='%.2f', wedgeprops=dict(width=0.5), shadow=True)
ax1.grid()
plt.show()