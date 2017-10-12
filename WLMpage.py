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


# @app.route('/_add_numbers')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     print(a + b)
#     return jsonify(result=a + b)


@app.route('/_pollWLM')
def readWLM():
    return jsonify(result=random.randint(0, 1000))

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/bokeh')
# def bokeh():
#     # init a basic bar chart:
#     # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
#     fig = figure(plot_width=600, plot_height=600)
#     fig.vbar(
#         x=[1, 2, 3, 4],
#         width=0.5,
#         bottom=0,
#         top=[1.7, 2.2, 4.6, 3.9],
#         color='navy'
#     )
#
#     # grab the static resources
#     js_resources = INLINE.render_js()
#     css_resources = INLINE.render_css()
#
#     # render template
#     script, div = components(fig)
#     html = render_template(
#         'bokeh.html',
#         plot_script=script,
#         plot_div=div,
#         js_resources=js_resources,
#         css_resources=css_resources,
#     )
#     return encode_utf8(html)


if __name__ == '__main__':
    app.run(debug=True)
