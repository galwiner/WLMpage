import random
import os
from flask import Flask, jsonify, render_template, request, json

import utilities.database_utilities as db
import utilities.WLM_utilities as wlm
import threading
import atexit
import datetime

# import json

POOL_TIME = 0.1  # Seconds

# variables that are accessible from anywhere
activeChannels = []
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()

wlm.WLMstart()


def create_app():
    app = Flask(__name__)

    def interrupt():
        global yourThread
        yourThread.cancel()

    def startup():
        cwd = os.path.dirname(__file__)
        dbname = 'wlm.db'
        DBPATH = os.path.join(cwd, 'utilities', dbname)
        db.create_database(DBPATH)

        yourThread = threading.Timer(POOL_TIME, doBackgroundTask, ())
        yourThread.start()

    def doBackgroundTask():
        global activeChannels
        global channelExposure
        global yourThread
        with dataLock:
            # Do your stuff with commonDataStruct Here
            activeChannels.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, doBackgroundTask, ())
        yourThread.start()

    startup()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app


app = create_app()


@app.route('/_pollWLM')
def readWLM():
    return jsonify(result=random.randint(0, 1000))


@app.route('/_getWLMData/')
def getWLMData():
    with dataLock:

        if len(activeChannels) > 1:
            # activeChannels=[i for i, e in enumerate(a) if e != 0]

            dat = {i: format(wlm.getFreqNum(i), '.5f') for i in range(1, 9)}

            return jsonify(dat)  # returning data from the server to the client works
            # return jsonify(result=my_var)
        else:
            return jsonify(result='Empty')


@app.route('/_setExposure', methods=['POST'])
def setExposureChan():
    chan = request.json['chan']
    e1 = request.json['e1']
    e2 = request.json['e2']
    wlm.setExposureModeNum(chan, 0)
    wlm.setExposureNum(1, e1, e2)
    print('set exposure')
    return json.dumps({'status': 'OK'})


@app.route('/_setWLMChannels', methods=['POST'])
def setWLMChannels():
    activeChannels = request.json['activeChannels']
    return json.dumps({'status': 'OK'})


@app.route('/_setchannelExposure', methods=['POST'])
def setchannelExposure():
    channelExposure = request.json['channelExposure']
    return json.dumps({'status': 'OK'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='192.168.0.101', port='5000')
    app.run(host='10.10.10.3', port='5000')
    # app.run(debug=True)
# working code to get frequency for WLM

# r.lib.Operation(r.cCtrlStartMeasurement)
# r.lib.SetSwitcherMode(1)
# get_wavelength = r.lib.GetFrequencyNum
# get_wavelength.restype = c_double
# freq = get_wavelength(1,0)
