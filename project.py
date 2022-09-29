import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from wave import Wave
import numpy as np
from PIL import Image as im





 

def main():
    def reset(event):
        freq_slider.reset()
        amp_slider.reset()

    def update(val, Wave):
        Wave.amp(amp_slider.val)
        Wave.compress(freq_slider.val)
        line.set_ydata(Wave.calculate(t))
        fig.canvas.draw_idle()

    def updateR(val):
        update(val, Wave=red)
    
    # phase, amplitude frequency
    red = Wave(0, 1, 1)
    blue = Wave(2, 1, 1)
    green = Wave(4, 1, 1)

    # define time range
    t = np.linspace(0, 1, 1000)

    fig, ax = plt.subplots()

    # define waves
    lineR = ax.plot(t, red.calculate(t), lw=2)
    lineG = ax.plot(t, green.calculate(t), lw=2)
    lineB = ax.plot(t, blue.calculate(t), lw=2)

    # leave space for slider
    ax.set_xlabel('Time [s]')
    fig.subplots_adjust(left=0.25, bottom=0.25)

    # frequency slider properties
    freqR = [0.25, 0.1, 0.65, 0.03]

    # Make a horizontal slider to control the frequency.
    axfreq = fig.add_axes(freqR)
    freq_slider = Slider(
        ax=axfreq,
        label='Frequency [Hz]',
        valmin=0.1,
        valmax=30,
        valinit=red.freq,
    )
    
    # amplitude slider properties
    ampR = [0.1, 0.25, 0.0225, 0.63]

    # Make a vertically oriented slider to control the amplitude
    axamp = fig.add_axes(ampR)
    amp_slider = Slider(
        ax=axamp,
        label="Amplitude",
        valmin=0,
        valmax=10,
        valinit=red.amp,
        orientation="vertical"
    )

    # register the update function with each slider
    freq_slider.on_changed(updateR)
    amp_slider.on_changed(updateR)

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')
    
    button.on_clicked(reset)
    plt.show()


if __name__ == "__main__":
    main()