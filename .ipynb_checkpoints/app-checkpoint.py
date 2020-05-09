from flask import Flask, request, jsonify
from joblib import load

clf = load("clf.joblib")

app = Flask(__name__)

@app.route("/")
def status():
    return "Ready!"

@app.route("/predict", methods=["POST"])
def predict():
    data_dict = request.get_json()

    LengthVer = data_dict["LengthVer"]
    LengthDia = data_dict["LengthDia"]
    LengthCro = data_dict["LengthCro"]
    Height = data_dict["Height"]
    Width = data_dict["Width"]

    X_predict = [[LengthVer, LengthDia, LengthCro, Height, Width]]

    default = clf.predict(X_predict)[0]
    probabily_of_default = clf.predict_proba(X_predict)[0][1]

    return jsonify({
        "Predicted weight of the fish is": bool(default),
        "probabily_of_weight": float(probabily_of_default)
    })

if __name__ == "__main__":
    app.run(debug=True)