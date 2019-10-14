import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
##change the nun numeric into numeric
def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df
df0 = pd.read_csv('train.csv')
## check the nulls
nulls = pd.DataFrame(df0.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
##handling missing value
data = df0.select_dtypes(include=[np.number]).interpolate().dropna()
df = handle_non_numerical_data(data )
##find the corolation between the features and the target
correlations = data.corr()['SalePrice'].drop('SalePrice')
print(correlations)
#define therolshold to select the corolated value
abs_corrs = correlations.abs()
high_correlations = abs_corrs [abs_corrs > 0.7].index.values.tolist()
print(high_correlations)
##train the sytem
y = np.log(df.SalePrice)
x = df[high_correlations]
#if you want to consider all features
#x = data.drop(['SalePrice', 'Id'], axis=1)  
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.33)
##Build a linear model
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(x_train, y_train)
##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(x_test, y_test))
predictions = model.predict(x_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))
##visualize
actual_values = y_test
plt.figure(1)
plt.scatter(predictions, actual_values, alpha=.75,color='b')
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('Linear Regression Model')
plt.show()
