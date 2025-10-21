import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Redaing the data
x = pd.read_csv("1st-coding-assignment/sales_forecast_sample_expanded.csv")

# droping the rows where the Sales are missing
x.dropna(axis=0, subset=["Sales"], inplace = True)
# setting up the target and predictors
y = x.Sales
x.drop(['Sales'], axis=1, inplace=True)

# Dividing the data into Training and Validating subsets
x_train_full, x_val_full, y_train, y_val = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

# creating a function to calculate the MAE of the data
def scores(t_x, v_x, t_y, v_y):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(t_x, t_y)
    preds = model.predict(v_x)
    return mean_absolute_error(v_y, preds)

# Imputing the missing values and removing the missing values (if any) from the object columns

x_train_object = x_train_full.select_dtypes(include=['object'])
x_val_object = x_val_full.select_dtypes(include=['object'])

cols_with_missing = [col for col in x_train_object.columns if x_train_object[col].isnull().any()]
x_train_object.drop(cols_with_missing, axis=1, inplace=True)
x_val_object.drop(cols_with_missing, axis=1, inplace=True)

x_train_num = x_train_full.select_dtypes(exclude=['object'])
x_val_num = x_val_full.select_dtypes(exclude=['object'])

my_imputer = SimpleImputer(strategy='most_frequent')
imputed_x_train_num = pd.DataFrame(my_imputer.fit_transform(x_train_num))
imputed_x_val_num = pd.DataFrame(my_imputer.transform(x_val_num))

imputed_x_train_num.columns = x_train_num.columns
imputed_x_val_num.columns = x_val_num.columns

# now merging both the object and imputed number data frames
# point to note that since we removed a few rows from the object data frame so we will remove the extra rows in the number data frame

x_train = pd.merge(imputed_x_train_num, x_train_object, left_index=True, right_index=True, how="inner")
x_val = pd.merge(imputed_x_val_num, x_val_object, left_index=True, right_index=True, how="inner")

# getting the list of object cols
s = (x_train.dtypes == 'object')
object_cols = list(s[s].index)

# starting with One Hot Encoding
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(x_train[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(x_val[object_cols]))

OH_cols_train.index = x_train.index
OH_cols_valid.index = x_val.index

num_X_train = x_train.drop(object_cols, axis=1)
num_X_valid = x_val.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)

# the number of rows in OH_X_train and y_train (also OH_X_valid and y_val) are not same so making them same 
y_t = y_train.loc[OH_X_train.index]
y_v = y_val.loc[OH_X_valid.index]

# printing the MAE
print("The MAE from One Hot Encoding method is:")
print(f"{scores(OH_X_train, OH_X_valid, y_t, y_v):.2f}")
