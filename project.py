import matplotlib.pyplot as plt
from wave import Wave
from matplotlib import cm, image as mimg
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Button
import cv2


 
CM=0
pic=0
f1_ax2=0

def main():

    global CM
    global pic
    global f1_ax2

    
    lum_img = mimg.imread('MucioMelon.JPG')
    lum_img = mimg.imread('rgb.jpg')
    # img = lum_img[:, :, 0]
    img = mimg.imread('bw.jpg')

    fig1 = plt.figure()
    spec1 = gridspec.GridSpec(ncols=7, nrows=5, figure=fig1)
    f1_ax1 = fig1.add_subplot(spec1[0:4, 1:3])
    f1_ax2 = fig1.add_subplot(spec1[0:4, 3:6])
    plt.axis('off')
    f1_ax3 = fig1.add_axes([0.87, 0.05, 0.1, 0.075])
    save = Button(f1_ax3, 'save\n colormap')
    
    def store(val):
        cmap2lut(red, green, blue)
        test_LUT()
        
    save.on_clicked(store)
       

    f1_ax1.set_xlabel('Time [s]')
      
    # phase, amplitude frequency
    red = Wave('red')
    green = Wave('green')
    blue = Wave('blue')

    lineR, = red.line(f1_ax1)
    lineG, = green.line(f1_ax1)
    lineB, = blue.line(f1_ax1)

    ncmap = Lcolormap(red,green,blue)

    CM = fig1.colorbar(cm.ScalarMappable(cmap=ncmap), ax=f1_ax2)
    
    hrect1 = [0.2, 0, 0.6, 0.08]
    hrect2 = [0.2, 0.05, 0.6, 0.08]
    hrect3 = [0.2, 0.1, 0.6, 0.08]
    
    vrect1 = [0, 0.3, 0.05, 0.6]
    vrect2 = [0.03, 0.3, 0.05, 0.6]
    vrect3 = [0.06, 0.3, 0.05, 0.6]

    vrect4 = [0.92, 0.3, 0.05, 0.6]
    vrect5 = [0.89, 0.3, 0.05, 0.6]
    vrect6 = [0.86, 0.3, 0.05, 0.6]
    

    red.sliders(fig1, vrect4, vrect1, hrect1)
    green.sliders(fig1, vrect5, vrect2, hrect2)
    blue.sliders(fig1, vrect6, vrect3, hrect3)
    
    pic = f1_ax2.imshow(img, cmap=ncmap)

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
        ncmap = Lcolormap(red, green, blue)
        CM.remove()
        pic.remove()
        f1_ax2 = fig1.add_subplot(spec1[0:4, 3:6])
        plt.axis('off')
        CM = fig1.colorbar(cm.ScalarMappable(cmap=ncmap), ax=f1_ax2)
        pic = f1_ax2.imshow(img, cmap=ncmap)
        
    trigger1 = fig1.canvas.mpl_connect('motion_notify_event', update)
    trigger2 = fig1.canvas.mpl_connect('button_press_event', update)
    
    plt.show()

def Lcolormap(R,G,B):

        map = np.zeros(shape=(255,4), dtype=float)

        for i in range (255):
            t = i/255
            map[i][0]=R.f(t)
            map[i][1]=G.f(t)
            map[i][2]=B.f(t)
            map[i][3]=1
        colormap = ListedColormap(map)
        return colormap
 
def cmap2lut(R, G, B, filename='lut.bmp'):  

    colormap = np.zeros((256, 1, 3), dtype=np.uint8)

    for i in range (255):
        t = i/255
        colormap[i, 0, 2]= R.f(t)*255
        colormap[i, 0, 1]= G.f(t)*255
        colormap[i, 0, 0]= B.f(t)*255

    cv2.imwrite('lut.bmp', colormap)

def test_LUT(filename='lut.bmp'):
    
    lut = cv2.imread(filename)
    img_gray = cv2.imread('MucioMelon.JPG')
    im_color = cv2.LUT(img_gray, lut)

    cv2.imshow('color', im_color) 
    cv2.waitKey(0)   
    cv2.destroyAllWindows() 
   

   
if __name__ == "__main__":
    main()