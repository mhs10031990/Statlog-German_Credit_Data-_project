import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from q06_feature_preprocessing.build import q06_feature_preprocessing

path = 'data/GermanData.csv'

def q07_randomsearch_predict():
    
