import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class Wave:
    # initial values, unless stated
    def __init__(self, name, phase=0, amplitude=1, freq=1):
        self.name = name
        self.phase = phase
        self.amp = amplitude
        self.freq = freq
        self.t = np.linspace(0, 1, 1000)

    # update all values
    def update(self):
        self.phase = self.sliderP.val
        self.amp = self.sliderA.val
        self.freq = self.sliderF.val   

    # calculate y value for given x
    def f(self, t):
            y = self.amp * (np.sin(2 * np.pi * self.freq * (t + self.phase)))
            return y

    # return a 2Dline object using current parameters
    def line(self, ax = plt):
        waveLine = ax.plot(self.t, self.f(self.t), lw=2)
        return waveLine

    # return y values using current parameters
    def values(self):
        y = self.f(self.t)
        return [y]

    def sliders(self, fig, rectF='', rectA='', rectP=''):
        if rectF:
            self.fAxis = fig.add_axes(rectF, label=self.name + 'f')
            self.sliderF = Slider(
                ax = self.fAxis,
                label = self.fAxis._label,
                valmin=0.1,
                valmax=30,
                valinit=self.freq,
                orientation="vertical")
        if rectA:
            self.aAxis = fig.add_axes(rectA, label=self.name + 'a')
            self.sliderA = Slider(
                ax = self.aAxis,
                label = self.aAxis._label,
                valmin=0.1,
                valmax=30,
                valinit=self.amp,
                orientation="vertical")
        if rectF:
            self.pAxis = fig.add_axes(rectP, label=self.name + 'p')
            self.sliderP = Slider(
                ax = self.pAxis,
                label = self.pAxis._label,
                valmin=0,
                valmax=1,
                valinit=self.phase)

    # getters
    
    @property
    def phase(self):
        return self._phase

    @property
    def amp(self):
        return self._amp

    @property
    def freq(self):
        return self._freq

    def __str__(self):
        return (f"phase: {self.phase}, amplitude: {self.amp}, frequency: {self.freq}")   

    # setters
    @phase.setter
    def phase(self, value):
        if str(value).replace('.','').isdecimal():
            self._phase = value
        else:
            self._phase = 0
    
    @amp.setter
    def amp(self, value):
        if str(value).replace('.','').isdecimal():
            self._amp = value
        else:
            self._amp = 1

    @freq.setter
    def freq(self, value):
        if str(value).replace('.','').isdecimal():
            self._freq = value
        else:
            self._freq = 1

