import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from math import sin



map = np.zeros(shape=(255,4), dtype=float)
for i in range (255):
    map[i][0]=(sin(i/100)+1)/2
    map[i][1]=(sin((i+60)/100)+1)/2
    map[i][2]=(sin((i +120)/100)+1)/2
    map[i][3]=1

newcmp = ListedColormap(map)

fig, ax = plt.subplots()

cmap = newcmp(np.linspace(0, 1, 256))
# mesh = ax.pcolormesh(cmap)
# plt.colorbar(mesh, ax=ax)

fig.colorbar(cm.ScalarMappable(cmap=newcmp), ax=ax)


plt.show()



