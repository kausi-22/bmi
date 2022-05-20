#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/bmi', methods=['POST', 'GET'])
def bmi():
    return render_template('result.html')

@app.route('/result.html',methods=['POST','GET'])
def bmipred():
    int_features =[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    if prediction == 0:
        pred = 'Extremely Weak'
    elif prediction ==1:
        pred = "Weak"
    elif prediction ==2:
        pred ='Normal'
    elif prediction == 3:
        pred = 'Over Weight'
    elif prediction ==4:
        pred = "Obesity"
    elif prediction ==5:
        pred ='Extreme Obesity'
        
    output=pred
    
    return render_template('result.html', prediction_text=' Your body Weight is {}'.format(output))

    
if __name__ =="__main__":
    app.run(debug=True)


# In[ ]:




