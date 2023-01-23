import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
import pickle
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("predictive_maintenance.csv")
data.head()
data.info()

le = preprocessing.LabelEncoder()

data.pop(data.columns[0]) 
data = data.drop("Failure_Type", axis = 1)

dataPID = data["Product_ID"]
le.fit(dataPID)
dataPIDt = le.transform(dataPID)
data["Product_ID"] = dataPIDt

dataT = data["Type"]
le.fit(dataT)
dataTt = le.transform(dataT)
data["Type"] = dataTt
data.head()

target = data["Target"]
data = data.drop("Target", axis = 1)
target.head(208)

rfg = RandomForestRegressor()

rfg.fit(data.values,target.values)

pickle.dump(rfg, open('models/model.pkl', 'wb')) #Enregistrer le model