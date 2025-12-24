from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = int(request.form["smoker"])
        region_se = int(request.form["region_southeast"])
        region_sw = int(request.form["region_southwest"])

        features = np.array([[age, bmi, children, smoker, region_se, region_sw]])
        prediction = model.predict(features)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
