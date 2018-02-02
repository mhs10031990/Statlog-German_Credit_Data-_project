# Split

Now that you have imported the data, let's split data into target or dependent variable and feature or independent variables. We can use these variables later on to fit a model.

## Write a function `q05_split` that:
- Call the previous function from Question 3
- Use `train_test_split` function to split to X_train, X_test, y_train, y_test
- What would be the dependent variable here?

Tip: In practice, we denote dependent variables with capital X and target variable with small y.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path of the csv file location |
| test_size | float | optional | 0.2 | split into train and test |
| random_state | int | optional | 9 | fixing the randomness of the split |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X_train | DataFrame | Dataframe containing feature variables |
| X_test | DataFrame | Dataframe containing feature variables |
| y_train | Series/DataFrame | Target Variable |
| y_test | Series/DataFrame | Target Variable |
