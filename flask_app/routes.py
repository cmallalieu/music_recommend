from flask import request, jsonify, redirect, Flask
from flask_app.app import app
from run_get_ratings import run_get_ratings
from data_processing.get_similarity import get_similarity_rating
from run_get_profile import get_user_profile as get_user

@app.route("/api/get_similarity/<user1>/<user2>", methods=["GET"])
def get_similarity(user1, user2):
    ratings_df1 = run_get_ratings(user1)
    ratings_df2 = run_get_ratings(user2)
    similarity = get_similarity_rating(ratings_df1, ratings_df2)
    return jsonify(similarity=similarity)


@app.route("/api/get_chart_data/<username>", methods=["GET"])
def get_chart_data(username):
    chart_data = run_get_ratings(username)
    return chart_data

@app.route("/api/get_user_profile/<username>", methods=["GET"])
def get_user_profile(username):
    profile = get_user(username)
    return profile