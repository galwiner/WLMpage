from lsa import spectrometer
from ctypes import c_double, c_bool, c_long

r = spectrometer.Spectrometer()


def WLMstart():
    r.lib.Operation(r.cCtrlStartMeasurement)
    r.lib.SetSwitcherMode(1)


def getFreqChan(chan):
    get_freq = r.lib.GetFrequencyNum
    get_freq.restype = c_double
    return get_freq(chan, 0)


def setExposureNum(chan, exposure):
    set_exp = r.lib.SetExposureNum
    set_exp.restype = c_long
    ret = set_exp(chan, 1, exposure)
    return ret


def getExposureNum(chan):
    get_exp = r.lib.GetExposureNum
    get_exp.restype = c_long
    ret = get_exp(chan, 1, 0)
    return ret


def getExposureModeNum(chan):
    exp_mode = r.lib.GetExposureModeNum
    exp_mode.restype = c_long
    ret = exp_mode(chan, True)
    return ret


def setAutoExposureModeNum(chan, set):
    exp_mode = r.lib.SetExposureModeNum
    exp_mode.restype = c_long
    ret = exp_mode(chan, set)
    return ret


def getSwitcherMode():
    mode = r.lib.GetSwitcherMode
    mode.restype = c_long
    ret = mode(0)
    return ret


def setSwitcherMode(set):
    mode = r.lib.SetSwitcherMode
    mode.restype = c_long
    ret = mode(set)
    return ret


# def setAutoExposure(chan):
#     #TODO implement an auto exposure feature. should work the same as it does in the desktop software - increase exposure from 0 until you get something
#     # not sure how the two channels need to be increased. one by one? check how it works in the desktop version.
#     pass

if __name__ == '__main__':
    r = spectrometer.Spectrometer()
    WLMstart()
    print(getFreqChan(1))
    # setExposure(1,50)
    # print(getExposure(1))
    print(SetAutoExposure(True, 1))
