import pandas as pd
from flask import Flask, request, render_template,jsonify
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired
from joblib import load
import numpy as np

clf = load("clf.joblib")

app = Flask(__name__)

@app.route("/")
def status():
    return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     data_dict = request.get_json()

#     Length1 = data_dict["Length1"]
#     Length2= data_dict["Length2"]
#     Length3 = data_dict["Length3"]
#     Height = data_dict["Height"]
#     Width = data_dict["Width"]

#     X_predict = [[Length1, Length2, Length3, Height, Width]]

#     weight_predicted = clf.predict(X_predict)[0]
#     probabily_of_weight_prediction = clf.predict_proba(X_predict)[0][1]

#     return jsonify({
#         "Predicted weight of the fish is": weight_predicted,
#         "probabily_of_weight": float(probabily_of_weight_prediction)
#     })

# Created a route to display the predicted weight for hold out data in table format
@app.route("/predict_weight")
def predict_weight():
    # Please enter the path for file to hold out fish data csv file
    file_path = "fish_holdout_demo.csv"
    
    # Convert the hold out data values to dataframe and convert it to a list to predict the weight
    df_holdout = pd.read_csv(file_path)
    df_holdout = pd.get_dummies(df_holdout, drop_first = True)
    X_predict = df_holdout[['Length3', 'Height', 'Width', 'Species_Parkki', 'Species_Perch',
       'Species_Pike', 'Species_Roach', 'Species_Smelt', 'Species_Whitefish']].values

    weight_predicted = clf.predict(X_predict)
    pred_wt = weight_predicted.tolist()

    # species = df_holdout["Species"].tolist()
    length1 = df_holdout["Length1"].tolist()
    length2 = df_holdout["Length2"].tolist()
    length3 = df_holdout["Length3"].tolist()
    height = df_holdout["Height"].tolist()
    width = df_holdout["Width"].tolist()
    result = list(zip(
        # species,
        pred_wt, length1, length2, length3, height, width))
    # return jsonify(result)
    return render_template("weight.html", target=result)
    

if __name__ == "__main__":
    app.run(debug=True)