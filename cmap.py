import numpy as np
from matplotlib import pyplot as plt, image as mimg
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from math import sin

img = mimg.imread('MucioMelon.JPG')


map = np.zeros(shape=(255,4), dtype=float)
for i in range (255):
    map[i][0]=(sin(i/100)+1)/2
    map[i][1]=(sin((i+60)/100)+1)/2
    map[i][2]=(sin((i +120)/100)+1)/2
    map[i][3]=1

newcmp = ListedColormap(map)

lum_img = img[:, :, 0]

plt.imshow(lum_img, cmap=newcmp)


# fig, ax = plt.subplots()

# cmap = newcmp(img)
# mesh = ax.pcolormesh(cmap)
# plt.colorbar(mesh, ax=ax)



plt.show()



