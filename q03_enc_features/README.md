# How to deal with categorical features?

This assignment comprises of loading the structured data and applying some operations to it.

## Write a function `q03_encode_features` that :

- Call the previous function from Question 1 
- Make copy of the DataFrame and initialize a empty dictionary 
- Use `For loop` to iterate through the columns and check for categorical variable and perform a encoding techniques
- Use Labelencoder function to do the encoding technique
   
### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Dataframe | Dataframe with above operations inculcated |
| variable | Dictionary | Column names |
