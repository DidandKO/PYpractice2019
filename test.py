import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)
y = np.random.randint(1, 10, size = 7)


fig, ax = plt.subplots()

ax.bar(x, y, color = 'red')


fig.set_figwidth(12)    #  ширина и
fig.set_figheight(6)    #  высота "Figure"
fig.set_facecolor('floralwhite')
ax.set_facecolor('seashell')

plt.show()
