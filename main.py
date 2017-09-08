import os
import sys
import json
import numpy as np
import pandas as pd
from glob import glob

import flask
from flask import Flask, request, session, flash, url_for
from flask_migrate import Migrate

app = Flask(__name__,
            template_folder='templates')
app.secret_key = 'this is a little secret.'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


folders = glob(os.path.join('static, images, *'))

# route
@app.route("/")
def index():
    conditions = glob(os.path.join('static', 'images', '*'))
    conditions = [condition.split('/')[-1] for condition in conditions]
    return flask.render_template('index.html', conditions=conditions)

@app.route("/<condition_number>/")
def visualize(condition_number):
    n_stacks = len(glob(os.path.join('static', 'images', str(condition_number), '*.jpg')))
    return flask.render_template('voxel.html',
                                 condition_number=condition_number,
                                 n_stacks=n_stacks)
