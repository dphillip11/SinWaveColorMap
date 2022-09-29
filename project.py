import matplotlib.pyplot as plt
from wave import Wave


 

def main():

    fig, ax = plt.subplots()

    ax.set_xlabel('Time [s]')
    fig.subplots_adjust(left=0.2, bottom=0.3, right=0.8)
    
    # phase, amplitude frequency
    red = Wave('R', 0, 1, 7)
    green = Wave('G', 0.2, 4, 1)
    blue = Wave('B', 0.4, 2, 1)

    lineR, = red.line(ax)
    lineG, = green.line(ax)
    lineB, = blue.line(ax)
    
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
        red.update()
        green.update()
        blue.update()

        lineR.set_ydata(red.values())
        lineG.set_ydata(green.values())
        lineB.set_ydata(blue.values())
        fig.canvas.draw_idle()

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