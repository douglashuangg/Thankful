from flask import Flask, render_template, request, redirect, session
import user.models
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = "verysecret123"
# database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.user_login_system
# decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")

    return wrap


@app.route("/")
def landingpage():
    return render_template("homepage.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/user/login", methods=["POST"])
def log():
    return user.models.User().login()


@app.route("/user/signup", methods=["POST"])
def signup():
    return user.models.User().signup()


@app.route("/user/signout/")
def signout():
    return user.models.User().signout()


@app.route("/sendinfo")
def register():
    return render_template("signup.html")


@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)