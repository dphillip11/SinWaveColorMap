import matplotlib.pyplot as plt
from wave import Wave
from matplotlib import cm
from matplotlib.colors import ListedColormap
import numpy as np

 
CM=0

def main():
    global CM

    
    fig, ax = plt.subplots()

    ax.set_xlabel('Time [s]')
    fig.subplots_adjust(left=0.2, bottom=0.3, right=0.8)
    
    # phase, amplitude frequency
    red = Wave('R')
    green = Wave('G')
    blue = Wave('B')

    lineR, = red.line(ax)
    lineG, = green.line(ax)
    lineB, = blue.line(ax)

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
    CM = fig.colorbar(cm.ScalarMappable(cmap=ncmap), ax=ax)
    
    hrect1 = [0.2, 0, 0.6, 0.08]
    hrect2 = [0.2, 0.05, 0.6, 0.08]
    hrect3 = [0.2, 0.1, 0.6, 0.08]
    
    vrect1 = [0, 0.3, 0.08, 0.6]
    vrect2 = [0.05, 0.3, 0.08, 0.6]
    vrect3 = [0.1, 0.3, 0.08, 0.6]

    vrect4 = [0.92, 0.3, 0.08, 0.6]
    vrect5 = [0.87, 0.3, 0.08, 0.6]
    vrect6 = [0.82, 0.3, 0.08, 0.6]
    

    red.sliders(fig, vrect4, vrect1, hrect1)
    green.sliders(fig, vrect5, vrect2, hrect2)
    blue.sliders(fig, vrect6, vrect3, hrect3)

    def update(val):
        global CM
        red.update()
        green.update()
        blue.update()

        lineR.set_ydata(red.values())
        lineG.set_ydata(green.values())
        lineB.set_ydata(blue.values())
        ncmap=colormap()
        CM.remove()
        CM = fig.colorbar(cm.ScalarMappable(cmap=ncmap), ax=ax)

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