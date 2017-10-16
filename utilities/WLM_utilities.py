from lsa import spectrometer



if __name__ == '__main__':
    r = spectrometer.Spectrometer()



r.lib.Operation(r.cCtrlStartMeasurement)
r.lib.SetSwitcherMode(1)
get_wavelength = r.lib.GetFrequencyNum
get_wavelength.restype = c_double
freq = get_wavelength(1,0)