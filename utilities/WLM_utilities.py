from lsa import spectrometer
from ctypes import c_double, c_bool, c_long
import time

r = spectrometer.Spectrometer()


def WLMstart():
    r.lib.Operation(r.cCtrlStopAll)
    r.lib.Operation(r.cCtrlStartMeasurement)
    r.lib.SetSwitcherMode(1)
    [setExposureModeNum(i, 1) for i in range(1, 8)]


def getFreqNum(chan):
    get_freq = r.lib.GetFrequencyNum
    get_freq.restype = c_double
    return get_freq(chan, 0)


def setExposureNum(chan, e1,e2):
    # set the exposure values of
    set_exp = r.lib.SetExposureNum
    set_exp.restype = c_long
    ret1 = set_exp(chan, 1, e1)
    ret2 = set_exp(chan, 2, e2)
    return [ret1,ret2]


def getExposureNum(chan):
    get_exp = r.lib.GetExposureNum
    get_exp.restype = c_long
    ret1 = get_exp(chan, 1, 0)
    ret2 = get_exp(chan, 1, 0)
    return [ret1,ret2]


def getExposureModeNum(chan):
    exp_mode = r.lib.GetExposureModeNum
    exp_mode.restype = c_long
    ret = exp_mode(chan, True)
    return ret


def setExposureModeNum(chan, set):
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

def getSwitcherChannel():
    getChan = r.lib.GetSwitcherChannel
    getChan.restype = c_long
    ret = getChan(0)
    return ret

def setSwitcherChannel(chan):
    setChan = r.lib.SetSwitcherChannel
    setChan.restype = c_long
    ret = setChan(chan)
    return ret


def setSwitcherSingals(listOfChans):
    '''set the channels the WLM cycles through when in switcher mode'''
    pass

# def setAutoExposure(chan):
#     #TODO implement an auto exposure feature. should work the same as it does in the desktop software - increase exposure from 0 until you get something
#     # not sure how the two channels need to be increased. one by one? check how it works in the desktop version.
#     pass

if __name__ == '__main__':
    r = spectrometer.Spectrometer()
    WLMstart()
    print(getFreqNum(1))
    # setExposure(1,50)
    # print(getExposure(1))
    print(SetAutoExposure(True, 1))
