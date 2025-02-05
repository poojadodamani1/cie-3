# -*- coding: utf-8 -*-
"""cie-3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KP2gYH2uaqSVJXqvwk-mnTHYg_xT1b66
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
data=fetch_california_housing()
data

df=pd.DataFrame(data.data,columns=data.feature_names)
df['PRICE']=data.target
df.head()

df.describe()

df.info()

df.isnull().sum()

X=df.drop('PRICE',axis=1)
Y=df['PRICE']=data.target
X
Y

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=5,test_size=0.5)
X_train

Y_train

Model=LinearRegression()
Model.fit(X_train,Y_train)
LinearRegression()

Y_pred=Model.predict(X_test)
Y_pred

Mse=mean_squared_error(Y_pred,Y_test)
Mse

rscore=r2_score(Y_pred,Y_test)
rscore