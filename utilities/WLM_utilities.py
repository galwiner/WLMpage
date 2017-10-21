from lsa import spectrometer
from ctypes import c_double

r = spectrometer.Spectrometer()


def WLMstart():
    r.lib.Operation(r.cCtrlStartMeasurement)
    r.lib.SetSwitcherMode(1)




def getFreqChan(chan):
    get_freq = r.lib.GetFrequencyNum
    get_freq.restype = c_double
    return get_freq(chan, 0)


def setExposure(chan,exposure):
    set_exp = r.lib.SetExposureNum
    set_exp.restype = c_double
    ret=set_exp(chan,1,50)
    return ret


if __name__ == '__main__':
    r = spectrometer.Spectrometer()
    WLMstart()
    print(getFreqChan(1))
