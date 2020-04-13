from flask import Flask, request, jsonify, render_template, redirect
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify("Pong!")

@app.route("/api/Laso/", methods=["POST"])
def test1():
    name = request.form["name"]
   




    print(name)
    return jsonify({"status": "success Laso"}), 201

@app.route("/api/LinReg/", methods=["POST"])
def test2():
    name = request.form["name"]
    target = request.form["target"]
    test_size = request.form["test_size"]
    dataset = request.files["dataset"]
    USAhousing = pd.read_csv(dataset)
    print(USAhousing.head())
    X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
    y = USAhousing['Price']
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(test_size), random_state=101)
    from sklearn.linear_model import LinearRegression
    lm = LinearRegression()
    lm.fit(X_train,y_train)
    print("Linear model intercept")
    print(lm.intercept_)
    coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
    print(coeff_df)
    
    predictions = lm.predict(X_test)
    plt.figure()
    plt.scatter(y_test,predictions)
    plt.show()
    cv2.waitKey(0)
    # sns.distplot((y_test-predictions),bins=50);
    from sklearn import metrics
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

    print(test_size)
    print(name)
    return jsonify({"status": "success LinearReg","rmse":np.sqrt(metrics.mean_squared_error(y_test, predictions))}), 201

@app.route("/api/BayReg/", methods=["POST"])
def test3():
    name = request.form["name"]
    print(name)
    return jsonify({"status": "success Bayesian Ridge"}), 201

@app.route("/api/Ridge/", methods=["POST"])
def test4():
    name = request.form["name"]
    print(name)
    return jsonify({"status": "success Ridge"}), 201


@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response

if __name__ == "__main__":
    app.run(debug=True)
