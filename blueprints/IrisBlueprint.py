from flask import Blueprint, jsonify, Response
import numpy as np
import pandas as pd
import os
import json

## GETTING THE DATASET PATH
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(APP_ROOT, 'data/iris.data')

## CREATE THE BLUEPRINT
IrisBlueprint = Blueprint('IrisBlueprint', __name__, template_folder='templates', static_folder='static')

## ROUTE TO GET THE IRIS FULL DATASET IN JSON FORMAT
@IrisBlueprint.route('/iris/dataset/')
def getDataSet():
    data = pd.read_csv(DATASET_PATH)
    iris_data = []
    for i in range(len(data.values)):
        iris_data.append({ 'sepal-length': data.values[i][0], 'sepal-width': data.values[i][1], 'petal-length': data.values[i][2], 'petal-width': data.values[i][3], 'class-name': data.values[i][4] })
    return Response(json.dumps(iris_data), mimetype='application/json')