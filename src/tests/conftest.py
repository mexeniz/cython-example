import os
import sys
import inspect
CURRENT_DIR = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
# Include paths for module search
sys.path.insert(0, PARENT_DIR)

import pytest

from myapi import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        # databases and resourses have to be freed at the end. But so far we don't have anything
        pass

    request.addfinalizer(teardown)
    return test_client
