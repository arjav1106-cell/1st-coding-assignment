# 1st-coding-assignment
Write three Python Scripts to do Ordinal Encoding, One Hot Encoding, and Imputation Techniques using basic Python functions and Numpy and Pandas libraries, but no pre-defined functions ( eg. get_dummies ).
<br>
Author - Arjav Jain
<br>
I have used the example of predicting the sales of a company. I saved a csv file in the folder named '1st-coding-assignment' with the data in it. My target variable in the given data is "Sales".
## 1) Ordinal Encoding
Instead of going with the simpler approach of removing the rows with the missing values, I used Imputation methods to impute the data. I only imputed the data of the numerical columns and not the object columns. For the missing values in the object columns, I just removed those rows. Then I merged both the imputed numerical columns and the object columns (with no row having missing values). I only kept the rows that were common to both the data frames that I merged, and not the extras. Finally, I made sure that the number of rows in the final merged predictors data frame and the target data frames are equal. Then found the MAE.
## 2) One Hot encoding
I have used a similar approach as I used in the Ordinal Encoding method.
## 3) Pipeline Method
Since learning to use Pipelines is important I have tried using Pipeline to cut short the code for both the categorical data handeling. I have created 2 functions each for Ordinal and One Hot Encoding and coded them using Pipelines.
## 4) Imputation Method
In Inputation methods (handling missing values in a data set) i have created seperate functions for each type of handling method. To note: I have commented out the Drop column method because the in the csv file's data all the columns have missing values somewher or the other so please just check the code running it will give an error.
