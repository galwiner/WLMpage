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


if __name__ == '__main__':
    r = spectrometer.Spectrometer()
    WLMstart()
    getFreqChan(1)
