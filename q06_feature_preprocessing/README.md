# Look out for most important features with respect to target variable

That's quite an impressive streak you have achieved.

Now let's look at most important features.Since you have learned the technique of selecting `k best features`.

## Write a function `q06_feature_preprocessing` that:

- Call the previous function from Question 5
- Initiate `MinMaxScaler`, `SMOTE`, `SelectKBest` to a variable.
- Scale the X_train and transform the X_test
- Use Smote only for the training set 
- Use KBest to select the top feature

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path of the csv file location |
| Kind | string | optional | regular | Smote method  |
| random_state | int | optional | 9 | fixing the randomness in the SMOTE function |
| k | int |optional | 8 | select the Kbest features

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X_train | DataFrame | Dataframe containing feature variables after Kbest and Smote |
| X_test | DataFrame | Dataframe containing feature variables after Kbest |
| y_train | Series/DataFrame | Target Variable after SMOTE |
| y_test | Series/DataFrame | Target Variable |


