import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q03_encode_features(path):
    df = q01_load_data_and_add_column_names(path)
    result = df.copy()
    encoders = {}
    for column in result.columns:
        if result.dtypes[column] == np.object:
            encoders[column] = LabelEncoder()
            result[column] = encoders[column].fit_transform(result[column])
    return result, encoders
