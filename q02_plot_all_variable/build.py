import pandas as pd
import numpy as np
import sys, os
from math import ceil
import matplotlib.pyplot as plt
plt.switch_backend('agg')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q02_plot_all_variable(path, cols=5):
    "write your solution here"
    df = q01_load_data_and_add_column_names(path)
    fig = plt.figure(figsize=(20, 15))
    rows = ceil(float(df.shape[1]) / cols)
    for i, column in enumerate(df.columns):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(column)
        if df.dtypes[column] == np.object:
            df[column].value_counts().plot(kind="bar", axes=ax)
        else:
            df[column].hist(axes=ax)
            plt.xticks(rotation="vertical")
    plt.subplots_adjust(hspace=0.7, wspace=0.2)
    plt.show()
