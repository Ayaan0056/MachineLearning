import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import datasets
import matplotlib.pyplot as plt


#creating model
data = pd.read_csv("homeprice.csv")
area = data.area
price = data.price 
model = linear_model.LinearRegression()
model.fit(data[['area']],data.price)

#Saving model using Pickle 
import pickle

with open('model_pickle', 'wb') as f:
    pickle.dump(model,f)