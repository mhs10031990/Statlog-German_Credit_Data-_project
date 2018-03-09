import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_plot_all_variable
from inspect import getfullargspec

path = 'data/GermanData.csv'
df = q02_plot_all_variable(path)


class Test_plot_all_features(TestCase):
    def test_args(self):
        arg = getfullargspec(q02_plot_all_variable).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (2, len(arg)))

    def test_defaults(self):
        args = getfullargspec(q02_plot_all_variable)
        self.assertEqual(args[3], (5,), "Expected default values do not match given default values")
