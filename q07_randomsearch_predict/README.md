# Build your own model

Now you are well aware of the different Models and hyperparameter techniques.
You are free to use any model you want to apply which has been taught to you.

## Write a function `q07_randomsearch_predict` that:

- Call the previous function from Question 6
- Build your own model and return the `roc_auc_score` at the end which should be greater than 0.63.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path of the csv file location |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| roc_auc_score | float | ROC AUC score |