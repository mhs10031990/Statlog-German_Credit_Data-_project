import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.model_selection import train_test_split
from q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q05_split(path, test_size=0.20, random_state=9):
    "write your solution here"
    encode_data, _ = q03_encode_features(path)
    X = encode_data.iloc[:, :-1]
    y = encode_data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
