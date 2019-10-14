import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('train.csv')
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

df = handle_non_numerical_data(df)
## check the nulls
nulls = pd.DataFrame(df.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
# print(nulls)
correlations = df.corr()['SalePrice'].drop('SalePrice')
#print(correlations)

#define therolshold to select the corolated value
abs_corrs = correlations.abs()
high_correlations = abs_corrs [abs_corrs > 0.7].index.values.tolist()
print(high_correlations)
##train the sytem
x = df[high_correlations]
y = df['SalePrice']
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.33)

#we will use gausian to predict
GausNB = GaussianNB()
GausNB.fit(x_train, y_train)
y_pred = GausNB.predict(x_test)
Naive=accuracy_score (y_test, y_pred)*100
print("Naïve Bayes accuracy is:", Naive)

#svc
svc = SVC(gamma='auto')
svc.fit(x_train, y_train)
Y_pred = svc.predict(x_test)
acc_svc = round(svc.score(x_test, y_test) * 100, 2)
print("svm accuracy is:", acc_svc)
#print(classification_report(y_test, y_pred))
#KNN
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(x_train, y_train)
Y_pred = knn.predict(x_test)
acc_knn = round(knn.score(x_train, y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)

