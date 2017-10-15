import random

# from bokeh.embed import components
# from bokeh.plotting import figure
# from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8

import os

from flask import Flask, jsonify, render_template, request

import utilities.database_utilities as db

cwd = os.path.dirname(__file__)
dbname = 'wlm.db'
DBPATH=os.path.join(cwd, 'utilities',dbname)

db.create_database(DBPATH)


app = Flask(__name__)


@app.route('/_pollWLM')
def readWLM():
    return jsonify(result=random.randint(0, 1000))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
# working code to get frequency for WLM

#r.lib.Operation(r.cCtrlStartMeasurement)
#r.lib.SetSwitcherMode(1)
#get_wavelength = r.lib.GetFrequencyNum
#get_wavelength.restype = c_double
#freq = get_wavelength(1,0)
