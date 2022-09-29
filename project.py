import matplotlib.pyplot as plt
from wave import Wave
from matplotlib import cm, image as mimg
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider, Button
import csv

 
CM=0
pic=0
f1_ax2=0

def main():

    global CM
    global pic
    global f1_ax2
    # img = mimg.imread('MucioMelon.JPG')
    # lum_img = img[:, :, 0]
    lum_img = mimg.imread('bw.jpg')

    fig1 = plt.figure()
    spec1 = gridspec.GridSpec(ncols=2, nrows=1, figure=fig1, bottom=0.3, left=0.2, right= 0.8)
    f1_ax1 = fig1.add_subplot(spec1[0, 0])
    f1_ax2 = fig1.add_subplot(spec1[0, 1])
    plt.axis('off')
    f1_ax3 = fig1.add_axes([0.87, 0.05, 0.1, 0.075])
    save = Button(f1_ax3, 'save\n colormap')
    
    

    f1_ax1.set_xlabel('Time [s]')
      
    # phase, amplitude frequency
    red = Wave('red')
    green = Wave('green')
    blue = Wave('blue')

    lineR, = red.line(f1_ax1)
    lineG, = green.line(f1_ax1)
    lineB, = blue.line(f1_ax1)

    def colormap():
        map = np.zeros(shape=(255,4), dtype=float)
        for i in range (255):
            t = i/255
            map[i][0]=red.f(t)
            map[i][2]=blue.f(t)
            map[i][1]=green.f(t)
            map[i][3]=1
        ncmap = ListedColormap(map)
        return ncmap

    def store(val):
        cmap2csv(colormap())
    save.on_clicked(store)
    
    ncmap=colormap()
    CM = fig1.colorbar(cm.ScalarMappable(cmap=ncmap), ax=f1_ax2)
    
    hrect1 = [0.2, 0, 0.6, 0.08]
    hrect2 = [0.2, 0.05, 0.6, 0.08]
    hrect3 = [0.2, 0.1, 0.6, 0.08]
    
    vrect1 = [0, 0.3, 0.08, 0.6]
    vrect2 = [0.05, 0.3, 0.08, 0.6]
    vrect3 = [0.1, 0.3, 0.08, 0.6]

    vrect4 = [0.92, 0.3, 0.08, 0.6]
    vrect5 = [0.87, 0.3, 0.08, 0.6]
    vrect6 = [0.82, 0.3, 0.08, 0.6]
    

    red.sliders(fig1, vrect4, vrect1, hrect1)
    green.sliders(fig1, vrect5, vrect2, hrect2)
    blue.sliders(fig1, vrect6, vrect3, hrect3)
    
    pic = f1_ax2.imshow(lum_img, cmap=ncmap)

    def update(val):
        global f1_ax2
        global CM
        global pic
        red.update()
        green.update()
        blue.update()

        lineR.set_ydata(red.values())
        lineG.set_ydata(green.values())
        lineB.set_ydata(blue.values())
        ncmap=colormap()
        CM.remove()
        pic.remove()
        f1_ax2 = fig1.add_subplot(spec1[0, 1])
        plt.axis('off')
        CM = fig1.colorbar(cm.ScalarMappable(cmap=ncmap), ax=f1_ax2)
        pic = f1_ax2.imshow(lum_img, cmap=ncmap)
        
    trigger1 = fig1.canvas.mpl_connect('motion_notify_event', update)
    trigger2 = fig1.canvas.mpl_connect('button_press_event', update)
    
    plt.show()
 
def cmap2csv(cmap, filename='colormap.csv'):   
    cols = cmap(np.ones((255,3)))
    cols = (cols * 255).astype(int)
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for col in cols:
            writer.writerow(col[0][:3])

 

   
if __name__ == "__main__":
    main()