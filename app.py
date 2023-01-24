# https://youtu.be/l3QVYnMD128
"""
Application that predicts heart disease percentage in the population of a town
based on the number of bikers and smokers. 

Trained on the data set of percentage of people biking 
to work each day, the percentage of people smoking, and the percentage of 
people with heart disease in an imaginary sample of 500 towns.

"""


import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn import preprocessing
import csv

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('models/model2.pkl', 'rb'))

#Define the route to be home. 
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory. 
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder. 

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')
    #return render_template('visualiser.js')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
@app.route('/predict',methods=['POST'])
def predict():
    
    #int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    int_features = [x for x in request.form.values()] #Convert string inputs to float.
    infos=int_features
    #**********************************
    dict_info={"product_ID":infos[0],"type":infos[1],
               "Air_temperature":infos[2],"Process_temperature":infos[3],
               "Rotational_speed":infos[4],
               "Torque":infos[5],"Tool_wear":infos[6]}
    data=[dict_info]
    df = pd.DataFrame(data)
    df.to_csv('data/data.csv', index=False, header=True)
    #***********************************
    Product_ID=int_features[0]
    int_features[0] = int_features[0][1:]
    #************************************
    if(int_features[1]=='L'):
        int_features[1]=0
    elif (int_features[1]=='M'):
        int_features[1]=1
    elif (int_features[1]=='H'):
        int_features[1]=2
    #************************************
    liste_infos=[float(x) for x in int_features]
    #***********************************
    features = [np.array(liste_infos)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]
    #*******************************************************
    if(prediction[0]>0.5):
        resultat="La machine avec ID: "+Product_ID+" va tomber en panne!!!"
    else:
        resultat="La machine avec ID: "+Product_ID+" est en bonne état"
    
    #return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))
    return render_template('dashboard.html', prediction_text=resultat,infos=infos)
    #return render_template('visualier.js',liste_info=int_features)


#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)