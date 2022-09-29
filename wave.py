import numpy as np
import matplotlib.pyplot as plt

class Wave:
    def __init__(self, phase=0, amplitude=1, freq=1):
        self.phase = phase
        self.amp = amplitude
        self.freq = freq
        self.t = np.linspace(0, 1, 1000)

    def __str__(self):
        return (f"phase: {self.phase}, amplitude: {self.amp}, frequency: {self.freq}")   

    def calculate(self, t):
            y = self.amp * (np.sin(2 * np.pi * self.freq * (t + self.phase)))
            return y

    def offset(self, x):
        self.phase = x

    def amplify(self, a):
        self.amp = a

    def compress(self, c):
        self.freq = c

    def plot(self):
        waveLine = plt.plot(self.t, self.calculate(self.t), lw=2)
        return waveLine

    def values(self):
        x = self.t
        y = self.calculate(x)
        return [x,y]

