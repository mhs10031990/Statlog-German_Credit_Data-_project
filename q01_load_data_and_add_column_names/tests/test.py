import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_load_data_and_add_column_names
from inspect import getfullargspec

path = 'data/GermanData.csv'
df = q01_load_data_and_add_column_names(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q01_load_data_and_add_column_names).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_type(self):
        self.assertEqual(df.shape, (1000, 21), "The Expected return type do not match with the return type")
