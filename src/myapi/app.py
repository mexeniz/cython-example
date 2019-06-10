from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    return 'OK'

@app.route('/normalize', methods=['POST'])
def normalize_post():
    pass

@app.route('/length', methods=['POST'])
def length_post():
    pass

@app.route('/predict', methods=['POST'])
def predict_post():
    pass