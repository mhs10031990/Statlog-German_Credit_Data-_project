import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE
from greyatomlib.statlog_german_credit_data_project.q05_split.build import q05_split
path = 'data/GermanData.csv'


def q06_feature_preprocessing():
    
    
