from ctypes import cdll, c_double, c_long, c_int, c_short, cast, POINTER
from os.path import join, exists
from time import sleep

from lsa import spectrometer
SYSTEM_FOLDERNAME = "C:\\Windows\\System32"
WLM_DATA_FILE = "wlmData.dll"
WLM_DATA_PATH = join(SYSTEM_FOLDERNAME, WLM_DATA_FILE)
WLM_FOLDERNAME = "C:\\Program Files (x86)\\HighFinesse\\Wavelength Meter WS7 1506"
HEADER_PATH = join(WLM_FOLDERNAME, "Projects\\Headers\\C", "wlmData.h")
SERVER_PATH = join(WLM_FOLDERNAME, "wlm_ws7.exe")
DATATYPE_MAP = {2: c_int, 4: c_long, 8: c_double}

class mySpectrometer(object):
    """
    A class for interacting with HighFinesse WLM. adapted from Catherine Holloway's work https://github.com/CatherineH
    """
    def __init__(self):
        self.errors_list = {}
        self.parse_header()
        if exists(WLM_DATA_PATH):
            self.lib = cdll.LoadLibrary(WLM_DATA_PATH)
            control_show = self.lib.ControlWLM(getattr(self, 'cCtrlWLMShow'), 0, 0)
            self.check_error(control_show, 'set')
            while not self.lib.Instantiate(getattr(self, 'cInstCheckForWLM')):
                pass
            connection = self.lib.Instantiate()
            self.check_error(connection, 'set')
        else:
            raise OSError("wlmData.dll not found in "+SYSTEM_FOLDERNAME)

    def parse_header(self):
        """
        Parse the values in the wlmData.h C header.
        :return: Nothing, values are added as attributes to the Spectrometer object
        """
        self.ranges = []
        if not exists(HEADER_PATH):
            raise OSError('Header file not found at ' + HEADER_PATH)
        f_in = open(HEADER_PATH, "r")
        begin_read = False
        for line in f_in.readlines():
            if line.find("Constants") > 0:
                begin_read = True
            if begin_read and line.find("const int") > 0:
                values = line.split("const int")[1].replace(";", "") \
                    .replace("\t", "").replace("\n", "") \
                    .split("//")[0].split(" = ")
                try:
                    # first, attempt to parse as int
                    setattr(self, values[0], int(values[1], 0))
                except ValueError:
                    parts = values[1].split(" + ")
                    # if that fails, parse as a value
                    value = 0
                    for part in parts:
                        try:
                            value += int(part, 0)
                        except ValueError:
                            value += getattr(self, part)
                    setattr(self, values[0], value)
                if values[0].find("Err") == 0:
                    if 'read' not in self.errors_list.keys():
                        self.errors_list['read'] = []
                    self.errors_list['read'].append(values[0])
                if values[0].find("ResERR") == 0:
                    if 'set' not in self.errors_list.keys():
                        self.errors_list['set'] = []
                    # no not append the "NoErr" Error
                    if getattr(self, values[0]) != 0:
                        self.errors_list['set'].append(values[0])
    def check_error(self, error_code, error_type='read'):
        """
        Check whether the value matches an error code
        :param error_code: the returned value from the call. Must be a float or int.
        :return: nothing
        """
        error_code = int(error_code)
        for error in self.errors_list[error_type]:
            if error_code == getattr(self, error):
                raise SpectrometerException(error)





def getFrequencies(spectrometer,wavelengthList):
    spectrometer.lib.Operation(spectrometer.cCtrlStartMeasurement)
    spectrometer.lib.SetSwitcherMode(1)
    get_wavelength = spectrometer.lib.GetFrequencyNum
    get_wavelength.restype = c_double

    freq = get_wavelength(1, 0)
    return freq





