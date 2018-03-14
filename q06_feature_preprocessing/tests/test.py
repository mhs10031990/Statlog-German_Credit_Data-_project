import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q06_feature_preprocessing
from inspect import getfullargspec

path = 'data/GermanData.csv'
df = q06_feature_preprocessing(path, kind="regular",random_state=9, k=8)


class Test_feature_preprocessing(TestCase):
    def test_args(self):
        arg = getfullargspec(q06_feature_preprocessing).args
        self.assertEqual(len(arg), 4, "Expected argument(s) %d, Given %d" % (4, len(arg)))

    def test_defaults(self):
        args = getfullargspec(q06_feature_preprocessing)
        self.assertEqual(args[3], (("regular",9,8)), "Expected default values do not match given default values")

    def test_return_train(self):
        self.assertEqual(df[0].shape, (1098, 8), "The Expected return type do not match with the return type")

    def test_return_test(self):
        self.assertEqual(df[1].shape, (200, 8), "The Expected return type do not match with the return type")
