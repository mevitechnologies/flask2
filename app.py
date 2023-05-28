from flask import Flask,redirect,url_for,render_template,request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import joblib
import pandas as pd 
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        StartAge=int(request.form['StartAge'])
        EndAge=int(request.form['EndAge'])
        menopause=int(request.form['menopause'])
        Starttumorsize=int(request.form['Starttumorsize'])
        endtumorsize=int(request.form['endtumorsize'])
        Start_env_nodes=int(request.form['Start_env_nodes'])
        end_env_nodes=int(request.form['end_env_nodes'])
        node_caps=int(request.form['node_caps'])
        deg_malig=int(request.form['deg_malig'])
        breast=int(request.form['breast'])
        breast_quad=int(request.form['breast_quad'])
        irradiat=int(request.form['irradiat'])
        data=[StartAge,EndAge,menopause,Starttumorsize,endtumorsize,Start_env_nodes,end_env_nodes,node_caps,deg_malig,breast,breast_quad,irradiat]
        data=np.array(data).reshape(1,-1)
        loaded_model = joblib.load('RandomForest_Logisticregression.pkl')
        predictions=loaded_model.predict(data)
        if predictions==[1]:
            result='<html><h1>Theres goona be a reoocurance of Breast Cancer</h1></html>'
        else:
            result='<html><h1>Theres goona be NO reoocurance of Breast Cancer</h1></html>'
        return result

if __name__ =="__main__":
    app.run(debug=True)