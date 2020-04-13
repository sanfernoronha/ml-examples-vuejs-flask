from flask import Flask, request, jsonify, render_template, redirect
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from pylab import savefig

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
    df = pd.read_csv(dataset)

    #directory making
    rootdirectory = name
    parent_dir = "/home/sanfer/Documents/ml-examples-vuejs-flask/web-app/src/assets/"
    path = os.path.join(parent_dir, rootdirectory)
    working = path #working path
    os.mkdir(path)

    plotdirectory = "plots"
    plot_parent_dir = parent_dir + rootdirectory + '/'
    path = os.path.join(plot_parent_dir, plotdirectory)
    plots_dir = path #plot path
    os.mkdir(path)

    # modeldirectory = "models"
    # model_parent_dir = parent_dir + rootdirectory + "/"
    # path = os.path.join(model_parent_dir, modeldirectory)
    # model_dir = path #model path
    # os.mkdir(path)





    #pre-processiong plots
   
    snsdist = sns.distplot(df[target])
    snsdist = snsdist.get_figure()
    snsdist.savefig(plots_dir + "/dist.png")
    snsdist.clf()

    


    dataTypes = df.dtypes
    for items in dataTypes.iteritems():
        # print(items)
        # print((items[1].name))
        if (items[1].name != 'float64' and items[1].name != 'int64'):
            df.drop(labels=items[0], axis=1, inplace=True)

    y = df[target]
    df.drop(labels=target, axis=1, inplace=True)
    df.replace(0, np.NaN).fillna(df.mean(), inplace=True)
    X = df[list(df.columns)]
   
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
    # plt.figure()
    plt.scatter(y_test, predictions)
    plt.savefig(plots_dir + "/scatter.png")
    plt.clf()

    sn = sns.distplot((y_test - predictions), bins=50)
    sn = sn.get_figure()
    sn.savefig(plots_dir + "/residual.png")
    sn.clf()
   

    # plt.show()
    # cv2.waitKey(0)
    # sns.distplot((y_test-predictions),bins=50);
    from sklearn import metrics
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
   
    print(test_size)
    print(name)

    #metrics to return
    r_square = lm.score(X, y)
    MAE = metrics.mean_absolute_error(y_test, predictions)
    MSE = metrics.mean_squared_error(y_test, predictions)
    RMSE = np.sqrt(MSE)


    #plot paths to return
    scatterplotpath = name + "/plots/scatter.png"
    distpath = name + "/plots/dist.png"
    residualpath = name + "/plots/residual.png"


    return jsonify({"status": "success LinearReg",
    "metrics": {
        "mae": MAE,
        "mse": MSE,
        "rmse": RMSE,
        "r_square": r_square
    },
    "ploturl": {
        "scatterplotpath": scatterplotpath,
        "distpath": distpath,
        "residualpath": residualpath
    }
    
    }), 201

@app.route("/api/BayReg/", methods=["POST"])
def test3():
    name = request.form["name"]
    target = request.form["target"]
    test_size = request.form["test_size"]
    dataset = request.files["dataset"]
    df = pd.read_csv(dataset)
    dataTypes = df.dtypes
    for items in dataTypes.iteritems():
        # print(items)
        # print((items[1].name))
        if (items[1].name != 'float64' and items[1].name != 'int64'):
            df.drop(labels=items[0], axis=1, inplace=True)

    y = df[target]
    df.drop(labels=target, axis=1, inplace=True)
    df.replace(0, np.NaN).fillna(df.mean(), inplace=True)
    X = df[list(df.columns)]
    
    
    
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
