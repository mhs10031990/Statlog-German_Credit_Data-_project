import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_split
from inspect import getfullargspec

path = 'data/GermanData.csv'
df = q05_split(path, test_size=0.20, random_state=9)


class Test_splits(TestCase):
    def test_args(self):
        arg = getfullargspec(q05_split).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

    def test_defaults(self):
        args = getfullargspec(q05_split)
        self.assertEqual(args[3], ((0.20,9)), "Expected default values do not match given default values")

    def test_returns_X_train(self):
        self.assertEqual(df[0].shape, (799, 20), "The Expected return type do not match with the return type")

    def test_returns_X_test(self):
        self.assertEqual(df[1].shape, (200, 20), "The Expected return type do not match with the return type")

    def test_returns_y_train(self):
        self.assertIsInstance(df[2],pd.Series, "The Expected return type do not match with the return type")

    def test_returns_y_test(self):
        self.assertIsInstance(df[3],pd.Series, "The Expected return type do not match with the return type")


