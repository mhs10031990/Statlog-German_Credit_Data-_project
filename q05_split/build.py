import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.model_selection import train_test_split
from q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q05_split():
    
