# How our data looks like ?

This assignment comprises of loading the structured data and applying some operations to it.

## Write a function `q01_load_data` that :
- Reads CSV file and convert CSV data to dataframe.
- Add columns names with below mentioned names
    - 'account_status', 'month', 'credit_history', 'purpose', 'credit_amount', 'savings_account/bonds', \
                  'employment', 'installment_rate', 'personal_status/sex', 'guarantors', 'residence_since', \
                  'property', 'age', 'other_installment_plans', 'housing', 'number_of_existing_credits', 'job',
                  'liable',
                  'telephone', 'foreign_worker', 'good/bad' 
- Map the last columns `good/bad` to 0, 1
- Return the DataFrame

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Dataframe | Dataframe with above operations inculcated |
