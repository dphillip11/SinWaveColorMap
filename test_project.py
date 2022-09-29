from wave import Wave
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

red = Wave()
green = Wave()
blue = Wave()
fig, ax = plt.subplots()

def main():
    layout()
    draw()
    
def layout():

    def update(val):
        
        red.amplify(sliders[axampR].val)
        blue.amplify(sliders[axampG].val)
        green.amplify(sliders[axampB].val)
        red.compress(sliders[axfreqR].val)
        blue.compress(sliders[axfreqG].val)
        green.compress(sliders[axfreqB].val)
        draw()
        fig.canvas.draw_idle()

    # leave space for slider    
    ax.set_xlabel('Time [s]')
    fig.subplots_adjust(left=0.3, bottom=0.3)    

    # vertical slider boxes
    vrect1 = [0, 0.3, 0.08, 0.6]
    axampR = fig.add_axes(vrect1, label='aR')
    vrect2 = [0.08, 0.3, 0.08, 0.6]
    axampG = fig.add_axes(vrect2, label='aG')
    vrect3 = [0.16, 0.3, 0.08, 0.6]
    axampB = fig.add_axes(vrect3, label='aB')

    # horizontal slider boxes
    hrect1 = [0.3, 0, 0.6, 0.08]
    axfreqR = fig.add_axes(hrect1, label='fR')
    hrect2 = [0.3, 0.08, 0.6, 0.08]
    axfreqG = fig.add_axes(hrect2, label='fG')
    hrect3 = [0.3, 0.16, 0.6, 0.08]
    axfreqB = fig.add_axes(hrect3, label='fB')

    # add frequency sliders
    sliders = {}
    axfreqs =[axfreqR,axfreqG,axfreqB]
    for axis in axfreqs:
        sliders[axis]= Slider(
            ax = axis,
            label = axis._label,
            valmin=0.1,
            valmax=30,
            valinit=1)
        sliders[axis].on_changed(update)

    # add amplitude sliders
    axamps =[axampR,axampG,axampB]
    for axis in axamps:
        sliders[axis]= Slider(
            ax = axis,
            label = axis._label,
            valmin=0.1,
            valmax=30,
            valinit=1,
            orientation="vertical")
        sliders[axis].on_changed(update)

    
    



 
def draw():
    ax.plot(red.values()[0],red.values()[1])
    ax.plot(green.values()[0],green.values()[1])
    ax.plot(blue.values()[0],blue.values()[1])
    plt.show()
    





if __name__ =="__main__":
    main()