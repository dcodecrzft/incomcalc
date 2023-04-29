from flask import Flask, request, render_template
import pandas
from sklearn.linear_model import LinearRegression


app = Flask(__name__)


@app.route("/")
def test():
    return render_template('index.html')
        
def PredictionModel(years_education:int, hours_per_week:int) -> float:
    df = pandas.read_csv("census-income.csv")

    years_education = abs(years_education)
    hours_per_week = abs(hours_per_week)
    
    X = df[[" education-num", " hours-per-week"]]
    y = df[" "].map({" <=50K":1, " >50K":0})

    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X.values, y)
    
    prediction = linear_regression_model.predict([[years_education, hours_per_week]])

    final_output = round(float(prediction[0]))

    return final_output




if __name__ == "__main__":
    app.run(debug=True)