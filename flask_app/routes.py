from flask import request, jsonify, redirect, Flask
from flask_app.app import app
from run import run
import startup

@app.route("/api/get_data/<username>", methods=["GET"])
def get_data(username):
    print(username)
    ratings_df = run(username)
    return ratings_df

@app.route("/api/test", methods=["GET"])
def test():
    return "test"

# @app.route('/')
# def index():
#     response = startup.getUser()
#     return redirect(response)

# @app.route('/callback/')
# def callback():
#     startup.getUserToken(request.args['code'])
#     redirect('/user')

