import pandas as pd

data = pd.read_csv(r"C:\Git programs\AIMS\1st-coding-assignment\ImputedData.csv")
new_data = data.copy()
# USING THE MAP FUNCTION
# columns to ordinal encode are ['Month','Online_Promotion','Product_Quality_Rating']
month_order_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}
Online_Promotion_order_map = {"Yes":1, "No":0}
Product_Quality_Rating_order_map = {"High":3,"Medium":2,"Low":1}

new_data['Month'] = new_data['Month'].map(month_order_map)
new_data['Online_Promotion'] = new_data['Online_Promotion'].map(Online_Promotion_order_map)
new_data['Product_Quality_Rating'] = new_data['Product_Quality_Rating'].map(Product_Quality_Rating_order_map)
# We can also use the '.replace()' function for this data

print(new_data)

# USING LOOP METHOD
# enter the data, order_map of the column that we want to encode and the column name of the column
def loop_method(data,order_map,column_name):
    new_data = data.copy()
    encoded_value = []
    for value in new_data[column_name]:
        code = order_map.get(value, None)
        encoded_value.append(code)
    new_data[column_name] = encoded_value
    return new_data
