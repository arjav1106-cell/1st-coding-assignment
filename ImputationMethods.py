import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
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

# removing the columns with dtypes as 'object'
x_train = x_train_full.select_dtypes(exclude='object')
x_val = x_val_full.select_dtypes(exclude='object')

cols_with_missing = [col for col in x_train.columns if x_train[col].isnull().any()]

def Dropcolumns():
    reduced_x_train = x_train.drop(cols_with_missing, axis=1)
    reduced_x_val = x_val.drop(cols_with_missing, axis=1)

    print(f"The MAE by using the Drop columns with missing vaule(simplest approach) method is: {scores(reduced_x_train,reduced_x_val,y_train,y_val):.2f}")

def Imputation():
    x_train_plus = x_train.copy()
    x_val_plus = x_val.copy()

    my_imputer = SimpleImputer(strategy='most_frequent')
    imputed_x_train = pd.DataFrame(my_imputer.fit_transform(x_train_plus))
    imputed_x_val = pd.DataFrame(my_imputer.transform(x_val_plus))

    imputed_x_train.columns = x_train_plus.columns
    imputed_x_val.columns = x_val_plus.columns

    print(f"The MAE by using the Imputation method is: {scores(imputed_x_train,imputed_x_val,y_train,y_val)}")

def ImputationExtension():
    x_train_plus = x_train.copy()
    x_val_plus = x_val.copy()
    
    for col in cols_with_missing:
        x_train_plus[col + '_was_missing'] = x_train_plus[col].isnull()
        x_val_plus[col + '_was_missing'] = x_val_plus[col].isnull()
    
    my_imputer = SimpleImputer(strategy='most_frequent')
    imputed_x_train = pd.DataFrame(my_imputer.fit_transform(x_train_plus))
    imputed_x_val = pd.DataFrame(my_imputer.transform(x_val_plus))

    imputed_x_train.columns = x_train_plus.columns
    imputed_x_val.columns = x_val_plus.columns

    print(f"The MAE by using the Extension to Imputation method is: {scores(imputed_x_train,imputed_x_val,y_train,y_val)}")

# Dropcolumns()
Imputation()
ImputationExtension()

'''I have commented out the Drop column method because the in the csv file's data all the columns have missing values somewher or the other so please just check the code running it will give an error'''