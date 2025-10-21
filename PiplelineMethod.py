import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Redaing the data
x = pd.read_csv("1st-coding-assignment/sales_forecast_sample_expanded.csv")

# droping the rows where the Sales are missing
x.dropna(axis=0, subset=["Sales"], inplace = True)
# setting up the target and predictors
y = x.Sales
x.drop(['Sales'], axis=1, inplace=True)

# Dividing the data into Training and Validating subsets
x_train_full, x_val_full, y_train, y_val = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

categorical_cols = [col for col in x_train_full.columns if x_train_full[col].nunique()<10 and x_train_full[col].dtype == 'object']
numerical_cols = [col for col in x_train_full.columns if x_train_full[col].dtype == ['int64','float64']]
my_cols = categorical_cols + numerical_cols

x_train = x_train_full[my_cols].copy()
x_val = x_val_full[my_cols].copy()

def OHEncode():
    numerical_transformer = SimpleImputer(strategy='mean')
    categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])

    processor = ColumnTransformer(transformers=[('num', numerical_transformer, numerical_cols), ('cat', categorical_transformer, categorical_cols)])

    model = RandomForestRegressor(n_estimators=100, random_state=0)

    my_pipeline = Pipeline(steps=[('preprocessor', processor),('model', model)])
    my_pipeline.fit(x_train, y_train)
    preds = my_pipeline.predict(x_val)
    scores = mean_absolute_error(y_val, preds)
    print(f"The score using One Hot encoding is: {scores:.2f}")

def OrdinalEncode():
    numerical_transformer = SimpleImputer(strategy='mean')
    categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),('ordinal', OrdinalEncoder())])

    processor = ColumnTransformer(transformers=[('num', numerical_transformer, numerical_cols), ('cat', categorical_transformer, categorical_cols)])

    model = RandomForestRegressor(n_estimators=100, random_state=0)

    my_pipeline = Pipeline(steps=[('preprocessor', processor),('model', model)])
    my_pipeline.fit(x_train, y_train)
    preds = my_pipeline.predict(x_val)
    scores = mean_absolute_error(y_val, preds)
    print(f"The score using Ordinal encoding is: {scores:.2f}")

OHEncode()
OrdinalEncode()
