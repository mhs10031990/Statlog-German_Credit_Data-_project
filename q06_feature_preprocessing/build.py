import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE
from q05_split.build import q05_split
path = 'data/GermanData.csv'


def q06_feature_preprocessing(path, kind="regular",random_state=9, k=8):
    "write your solution here"
    X_train, X_test, y_train, y_test = q05_split(path)
    scale = MinMaxScaler()
    smote = SMOTE(kind=kind, random_state=random_state)
    kbest = SelectKBest(k=k)

    X_train = scale.fit_transform(X=X_train)
    X_test = scale.transform(X=X_test)
    X_train_transform, y_train_transform = smote.fit_sample(X_train, y_train)
    kbest.fit(X_train_transform, y_train_transform)
    features_train = kbest.transform(X_train_transform)
    features_test = kbest.transform(X_test)
    return features_train, features_test, y_train_transform, y_test
