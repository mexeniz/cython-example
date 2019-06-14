import inspect
import os
import sys
CURRENT_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
# Include paths for module search
sys.path.insert(0, PARENT_DIR)

import numpy as np
import pytest

from myapi import vecutil

class TestVecUtil():

    def test_random_vec_success(self):
        length = 1
        vector = vecutil.random_vec(length)
        assert len(vector) == length

        length = 5
        vector = vecutil.random_vec(length)
        assert len(vector) == length
    
    def test_random_vec_fail(self):
        with pytest.raises(ValueError):
            length = -1
            vector = vecutil.random_vec(length)

        with pytest.raises(ValueError):
            length = 0
            vector = vecutil.random_vec(length)

        with pytest.raises(ValueError):
            length = 1.5
            vector = vecutil.random_vec(length)

    def test_normalize_vec(self):
        length = 5
        vector = vecutil.random_vec(length)
        norm_vec = vecutil.normalize_vec(vector)
        # Compare double value
        assert np.linalg.norm(norm_vec) - 1 < 0.00000001 