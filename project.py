import matplotlib.pyplot as plt
from wave import Wave
from matplotlib import cm, image as mimg
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.gridspec as gridspec

 
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
    spec1 = gridspec.GridSpec(ncols=2, nrows=1, figure=fig1, bottom=0.3, left=0.3, right= 0.7)
    f1_ax1 = fig1.add_subplot(spec1[0, 0])
    f1_ax2 = fig1.add_subplot(spec1[0, 1])
    plt.axis('off')

    f1_ax1.set_xlabel('Time [s]')
      
    # phase, amplitude frequency
    red = Wave('R')
    green = Wave('G')
    blue = Wave('B')

    lineR, = red.line(f1_ax1)
    lineG, = green.line(f1_ax1)
    lineB, = blue.line(f1_ax1)

    def colormap():
        map = np.zeros(shape=(255,4), dtype=float)
        for i in range (255):
            t = i/255
            map[i][0]=red.f(t)
            map[i][1]=blue.f(t)
            map[i][2]=green.f(t)
            map[i][3]=1
        ncmap = ListedColormap(map)
        return ncmap

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
        
        

    red.sliderF.on_changed(update)
    red.sliderA.on_changed(update)
    red.sliderP.on_changed(update)

    green.sliderF.on_changed(update)
    green.sliderA.on_changed(update)
    green.sliderP.on_changed(update)

    blue.sliderF.on_changed(update)
    blue.sliderA.on_changed(update)
    blue.sliderP.on_changed(update)
    
    
    plt.show()
 

    

   




if __name__ == "__main__":
    main()