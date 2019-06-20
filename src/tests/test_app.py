import inspect
import json
import os
import sys
CURRENT_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
# Include paths for module search
sys.path.insert(0, PARENT_DIR)

import numpy as np
import pytest

def json_of_response(res):
    """Decode json from response"""
    return json.loads(res.data.decode('utf8'))

class TestApp():

    def test_index_get(self, client):
        res = client.get('/')
        assert res.status_code == 200
        assert res.data == b'OK'

    def test_random_get(self, client):
        res = client.get('/random')
        assert res.status_code == 200
        
        json_data = json_of_response(res)
        assert 'random' in json_data
        assert type(json_data.get('random')) == list