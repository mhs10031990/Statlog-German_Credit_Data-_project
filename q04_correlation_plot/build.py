import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q04_correlation_plot():
   
