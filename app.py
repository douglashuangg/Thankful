from flask import Flask, render_template, request, redirect
from user.models import User
import pymongo

app = Flask(__name__)

# database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.user_login_system


@app.route("/")
def landingpage():
    return render_template("homepage.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/user/signup", methods=["POST"])
def signup():
    return User().signup()


@app.route("/sendinfo")
def register():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)