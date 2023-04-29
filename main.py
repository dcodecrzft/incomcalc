from flask import Flask, request, render_template, redirect, url_for
import pandas
from sklearn.linear_model import LinearRegression


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc/")
def calc(): 
    return render_template("calc.html")



def PredictionModel(years_education:int, hours_per_week:int) -> float:
    df = pandas.read_csv("census-income.csv")

    years_education = abs(int(years_education))
    hours_per_week = abs(int(hours_per_week))
    
    X = df[[" education-num", " hours-per-week"]]
    y = df[" "].map({" <=50K":1, " >50K":0})

    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X.values, y)
    
    prediction = linear_regression_model.predict([[years_education, hours_per_week]])

    final_output = round(float(prediction[0]))

    if final_output < 0:
        final_output = 0
        return final_output
    elif final_output > 1:
        final_output = 1
        return final_output
    else:
        return final_output



@app.route("/calc/prediction", methods=["POST"])
def predict():
    if request.method == 'POST':
        edu_num = request.form['edu']
        hrs = request.form['hrs']
        x = PredictionModel(edu_num, hrs)
        return f'<h1 style="font-family: sans-serif">Final Output = {x}</h1><br><h1 style="font-family: sans-serif">1: <=$50K  0: >$50K</h1>'


if __name__ == "__main__":
    app.run(debug=True)