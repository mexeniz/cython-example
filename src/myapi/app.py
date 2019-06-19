import inspect
import json
import os

from flask import Flask, request, Response

from . import clf
from . import vecutil

CURRENT_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

app = Flask(__name__)
predictor = None 

def load_model(pickle_path=None):
    global predictor
    if pickle_path is None:
        pickle_path = os.path.join(CURRENT_DIR, 'model.pkl')
    predictor = clf.Predictor(pickle_path)

@app.route('/', methods=['GET'])
def index_get():
    return 'OK'

@app.route('/normalize', methods=['POST'])
def normalize_post():
    req_data = request.json
    array = req_data.get('array')

    data = {
        'normalized' : vecutil.normalize_vec(array).tolist(),
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')


@app.route('/random', methods=['GET'])
def random_get():
    default_len = 5
    data = {
        'random' : vecutil.random_vec(default_len).tolist(),
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')


@app.route('/predict', methods=['POST'])
def predict_post():
    req_data = request.json
    feature = req_data.get('feature')
    
    data = {
        'predict' : predictor.predict([feature]).tolist(),
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')