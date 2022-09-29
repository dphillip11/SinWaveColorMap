import matplotlib.pyplot as plt
import csv
from matplotlib.colors import ListedColormap
import numpy as np
from matplotlib import cm, image as mimg


map = np.zeros(shape=(255,4), dtype=float)

with open('colormap.csv') as file:
    reader=csv.reader(file)
    i=0
    for row in reader:        
            map[i][0]=float(row[0])/255
            map[i][1]=float(row[1])/255
            map[i][2]=float(row[2])/255
            map[i][3]=1
ncmap = ListedColormap(map)
# img = mimg.imread('MucioMelon.JPG')
# lum_img = img[:, :, 0]
lum_img = mimg.imread('bw.jpg')  
plt.imshow(lum_img, cmap=ncmap)

plt.show()
        