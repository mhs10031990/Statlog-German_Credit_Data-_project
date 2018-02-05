import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q03_encode_features():

