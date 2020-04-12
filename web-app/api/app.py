from flask import Flask, request, jsonify, render_template, redirect
import os

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
    print(name)
    return jsonify({"status": "success LinearReg"}), 201

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
