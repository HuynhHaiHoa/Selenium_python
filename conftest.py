from collections import OrderedDict
import pytest
import json
import re
import glob
import os

def get_test_dict_from_json(data_file):
    with open(data_file) as f:
        try:
            d = json.load(f, object_pairs_hook=OrderedDict)
            metadata = d[0] if not d[0].get("test_id") else {}
            d = [dict(i, test_file=data_file) for i in d if i.get("test_id")]
            for k, v in metadata.iteritems():
                d = [i if i.get(k) else dict(i, **{k: v}) for i in d]
            return d
        except Exception as error:
            error.args = ("Failed to load test file, {0}: {1}".format(
                os.path.basename(data_file), error),)
            raise

def pytest_runtest_setup(item):
   """
   Fixture called before test run.
   """
   # Depending on pytest version attr is either '_testsfailed' or 'testsfailed'
   testsfailed = next(getattr(item.session, i) for i in dir(item.session) if i.endswith('testsfailed'))
   item.__testsfailed = testsfailed
   item.cls._funcargs = item.funcargs
   
def pytest_generate_tests(metafunc):
    """
    This function parametrizes tests.
    It reads the input data from data files that begin with the same name as the test method name.
    Each row of data needs to have a "test_id" key specifying the name of the test iteration.
    Each row of data is sent as a dict to the "params" input variable of the test.
    """
    test_dict = []
    base_name = os.path.join(os.path.dirname(metafunc.module.__file__), metafunc.function.__name__)

    function_files = glob.glob(base_name + "*.json")
    module_files = glob.glob(metafunc.module.__file__[:-2] + "json")
    data_files = function_files or module_files
    if "params" in metafunc.fixturenames and len(data_files):
        for data_file in data_files:
            d = get_test_dict_from_json(data_file)
            test_dict.extend(d)
        metafunc.parametrize("params", test_dict, ids=[i["test_id"] for i in test_dict])
        return

@pytest.fixture
def data_set(request):
   """
   Load test data from JSON and pass it on to test inside a dictionary.
   It reads the input data from data files that have the same base name as the test module name.
   Within that file, it will find the data that has a 'test_id' field matching the test method name.
   This provides a one-to-one mapping of JSON test_id to Python test method,
   as opposed to the regular parametrization technique, which is many-to-one.
   """
   data_file = request.module.__file__[:-2] + 'json'
   test_id = request.node.name

   with open(data_file) as f:
      d = json.load(f, object_pairs_hook=OrderedDict)
      data = next(i for i in d if i.get('test_id', '') == test_id)

   request._funcargs['params'] = data

