import pandas as pd

data = pd.read_csv(r"C:\Git programs\AIMS\1st-coding-assignment\ImputedData.csv")

# columns to encode by One Hot method
columns = ['Region','Product_Category','Store_Type']
def OHEncoder(data,columns):
    new_data = data.copy()
    for column in columns:
        categories = new_data[column].unique()
        for cat in categories:
            new_data[column + cat] = (new_data[column] == cat).astype(int)
        new_data.drop([column], inplace=True, axis=1)
    return new_data

new_data = OHEncoder(data, columns)
print(new_data)
