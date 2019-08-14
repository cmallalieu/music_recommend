from flask import request, jsonify, redirect, Flask
from flask_app.app import app
from run import run


@app.route("/api/get_similarities/<user1>/<user2>", methods=["GET"])
def get_data(user1, user2):
    ratings_df = run(user1)
    return ratings_df


@app.route("/api/get_chart_data/<username>", methods=["GET"])
def get_chart_data(username):
    chart_data = run(username)
    return chart_data