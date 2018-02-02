import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_randomsearch_predict
from inspect import getargspec

path = 'data/GermanData.csv'

df = q07_randomsearch_predict(path)

class Test_randomsearch_predict(TestCase):
    def test_args(self):
        arg = getargspec(q07_randomsearch_predict).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))


    def test_return_train(self):
        self.assertGreaterEqual(df, 0.63, "The Expected return type do not match with the return type")

