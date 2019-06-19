import inspect
import os
import sys
CURRENT_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
# Include paths for module search
sys.path.insert(0, PARENT_DIR)

import pytest

from myapi import clf
from myapi import vecutil

class TestPredictor():

    def test_init(self):
        model_path = os.path.join(CURRENT_DIR, 'mock_model.pkl')
        predictor = clf.Predictor(model_path)
    
    def test_predict(self):
        model_path = os.path.join(CURRENT_DIR, 'mock_model.pkl')
        predictor = clf.Predictor(model_path)
        
        length = 5
        features = vecutil.random_vec(length)
        predict_res = predictor.predict([features])
        print('Predict:', predict_res)
        assert len(predict_res) == 1
