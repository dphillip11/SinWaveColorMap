from project import Lcolormap, cmap2lut, check_LUT
import wave
import numpy as np
import os



def test_wave_params():
    testWave = wave.Wave('test_wave', phase=0, amplitude=1, freq= 1)
    assert testWave.f(0) == 1

def test_wave_params2():
    testWave = wave.Wave('test_wave')
    yVals = testWave.values()
    assert len(yVals[0]) == 255
    for i in range(len(yVals)):
        assert np.all(yVals[i] >= 0)
        assert np.all(yVals[i] <= 1)

def test_Lcolormap():
    black = wave.Wave('black', amplitude=0)
    lmap = Lcolormap(black,black,black)
    assert str(type(lmap)) == "<class 'matplotlib.colors.ListedColormap'>"

def test_cmap2lut():
    try:
        os.remove('test.bmp')
    except:
        pass
    black = wave.Wave('black', amplitude=0)
    cmap2lut(black,black,black, filename='test.bmp')
    with open('test.bmp') as file:
        assert file
    os.remove('test.bmp')

    
def test_check_LUT():
    black = wave.Wave('black', amplitude=0)
    cmap2lut(black,black,black, filename='test.bmp')
    check_LUT('test.bmp', Save=1)
    with open('MucioMelon.JPGtest.bmp') as file:
        assert file
    os.remove('MucioMelon.JPGtest.bmp')





