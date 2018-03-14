import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_encode_features
from inspect import getfullargspec

path = 'data/GermanData.csv'
df = q03_encode_features(path)


class Test_encode_features(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_encode_features).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_type(self):
        self.assertEqual(df[0].shape, (999, 21), "The Expected return type do not match with the return type")
