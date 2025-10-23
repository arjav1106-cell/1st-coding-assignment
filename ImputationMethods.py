import pandas as pd

data = pd.read_csv(r'C:\Git programs\AIMS\1st-coding-assignment\data.csv')

# removing the columns that have any missing data
def remove_col_with_missing(data):
    new_data = data.dropna(axis=1)
    return new_data

# removing the rows with the missing data
def remove_row_with_missing(data):
    new_data = data.dropna()
    return new_data

# IMPUTING NUMERICAL DATA
# imputing the missing values with the mean of the column
def imputing_mean_num(data):
    numerical_cols = [cols for cols in data.columns if data[cols].dtype in ['int64','float64']]
    new_data = data[numerical_cols].copy()
    for col in numerical_cols:
        new_data[col] = data[col].fillna(data[col].mean())
    return new_data

# imputing the missing values with the median of the column
def imputing_mediam_num(data):
    numerical_cols = [cols for cols in data.columns if data[cols].dtype in ['int64','float64']]
    new_data = data[numerical_cols].copy()
    for col in numerical_cols:
        new_data[col] = data[col].fillna(data[col].median())
    return new_data

# imputing the missing values with the mode of the column
def imputing_mode_num(data):
    numerical_cols = [cols for cols in data.columns if data[cols].dtype in ['int64','float64']]
    new_data = data[numerical_cols].copy()
    for col in numerical_cols:
        new_data[col] = data[col].fillna(data[col].mode()[0])
    return new_data

# imputing using linear interpolation
def imputing_interpolation_num(data):
    numerical_cols = [cols for cols in data.columns if data[cols].dtype in ['int64','float64']]
    new_data = data[numerical_cols].copy()
    for col in numerical_cols:
        new_data[col] = data[col].interpolate(method='linear')
    return new_data

# IMPUTING OBJECT DATA
# imputing unsing forward filling 
def imputing_ffill_obj(data):
    object_cols = [cols for cols in data.columns if data[cols].dtype == 'object']
    new_data = data[object_cols].copy()
    for col in object_cols:
        new_data[col] = data[col].fillna(method='ffill')
    return new_data

# imputing with backward filling
def imputing_bfill_obj(data):
    object_cols = [cols for cols in data.columns if data[cols].dtype == 'object']
    new_data = data[object_cols].copy()
    for col in object_cols:
        new_data[col] = data[col].fillna(method='bfill')
    return new_data
# note:- backward filling will not be helpful in this case since the last row of an object column has a missing value so it will be left as NaN

# imputing the missing values with the mode of the column
def imputing_mode_obj(data):
    object_cols = [cols for cols in data.columns if data[cols].dtype == 'object']
    new_data = data[object_cols].copy()
    for col in object_cols:
        new_data[col] = data[col].fillna(data[col].mode()[0])
    return new_data

# imputing the missing values with a constant 'Missing'
def imputing_missing_obj(data):
    object_cols = [cols for cols in data.columns if data[cols].dtype == 'object']
    new_data = data[object_cols].copy()
    for col in object_cols:
        new_data[col] = data[col].fillna('Missing')
    return new_data

# ADDING A COLUMN STATING THAT IS VALUE WAS MISSING IN FRONTY OF IT
def adding_missing_cols(data):
    cols_with_missing = [cols for cols in data.columns if data[cols].isnull().any()]
    new_data = data.copy()
    for col in cols_with_missing:
        new_data[col + '_was_missing'] = new_data[col].isnull()
    return new_data
# now we can run this function and then use any of the above imputaion functions for getting the final data frame

# SHOWING AN EXAMPLE OF USING THE FUNCTIONS AND IMPUTING THE DATA
df_with_added_cols = adding_missing_cols(data)
num_imputation = imputing_interpolation_num(df_with_added_cols)
obj_imputation = imputing_mode_obj(df_with_added_cols)
# now merging both the numerical and object data frames
imputed_data = pd.concat([num_imputation, obj_imputation], axis=1)
# the imputing_interpolation_num() and imputing_mode_obj() removed the boolean rows so adding them back
bool_df = df_with_added_cols.select_dtypes(include='bool')
final_imputed_data = pd.concat([imputed_data, bool_df], axis=1)
print(data)
print()
print(final_imputed_data)