import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from q06_feature_preprocessing.build import q06_feature_preprocessing

path = 'data/GermanData.csv'

def q07_randomsearch_predict(path):
    "write your solution here"
    gbc_ht = {'loss': ['deviance', 'exponential'],
              'learning_rate': [0.0001, 0.001, 0.01],
              'n_estimators': [100, 250, 300, 350],
              'max_depth': [7, 9, 12],
              'max_features': ['auto', 'sqrt', 'log2']}
    GBC = GradientBoostingClassifier(random_state=9)
    X_train, X_test, y_train, y_test = q06_feature_preprocessing(path)
    random_search = RandomizedSearchCV(estimator=GBC, param_distributions=gbc_ht , scoring='roc_auc', random_state=9)
    random_search.fit(X_train, y_train)
    pred = random_search.predict(X_test)
    return roc_auc_score(pred, y_test)
