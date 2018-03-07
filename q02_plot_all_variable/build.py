import pandas as pd
import numpy as np
import sys, os
from math import ceil
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.statlog_German_Credit_Data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q02_plot_all_variable():
    
