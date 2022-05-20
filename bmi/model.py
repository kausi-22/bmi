#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("bmi.csv")

LE = LabelEncoder()
data['Gender'] = LE.fit_transform(data['Gender'])
data['Index'] = LE.fit_transform(data['Index'])

X = data.drop('Index',axis =1)
Y = df["Index"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train, y_train)

pickle.dump(rfc, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


# In[ ]:




